#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CRISP-DM · Data Understanding (VS Code + Git)
Script: data_NNA.py
Descripción: Análisis descriptivo y exploratorio (EDA) minimalista que
             genera tablas e imágenes (gráficos) para una base Excel/CSV.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
from typing import Optional, Union, List, Dict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Utilidades locales
# ---------------------------------------------------------------------
def get_logger() -> logging.Logger:
    """Logger sencillo a consola."""
    logger = logging.getLogger("data_NNA")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        fmt = logging.Formatter("[%(levelname)s] %(message)s")
        ch.setFormatter(fmt)
        logger.addHandler(ch)
    return logger


def ensure_dir(path: str) -> None:
    """Crea el directorio si no existe (idempotente)."""
    os.makedirs(path, exist_ok=True)


def _detect_sep(csv_path: str, candidates: List[str] = [",", ";", "\t", "|"]) -> str:
    """Heurística simple para detectar separador en CSV."""
    with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
        head = f.readline()
    best_sep, best_count = ",", -1
    for s in candidates:
        cnt = head.count(s)
        if cnt > best_count:
            best_sep, best_count = s, cnt
    return best_sep


def read_any(path: str, sep: str = "auto", sheet: Optional[Union[int, str]] = None) -> pd.DataFrame:
    """
    Lee Excel o CSV con separador auto-detectado (si procede).
    Para Excel prueba header=0,1,2 hasta encontrar columnas válidas.
    """
    ext = os.path.splitext(path.lower())[1]

    # Archivos Excel
    if ext in [".xlsx", ".xls"]:
        for h in [0, 1, 2]:
            df = pd.read_excel(path, sheet_name=sheet, header=h)
            if df.shape[1] > 0:
                return df
        # fallback
        return pd.read_excel(path, sheet_name=sheet, header=None)

    # CSV u otros delimitados
    if sep == "auto":
        sep = _detect_sep(path)
    return pd.read_csv(path, sep=sep, low_memory=False, encoding="utf-8")


def data_overview(df: pd.DataFrame) -> Dict[str, object]:
    """Resumen básico: dimensiones, columnas, dtypes, nulos, memoria."""
    rows, cols = df.shape
    dtypes = df.dtypes.astype(str).value_counts().to_dict()
    missing = int(df.isna().sum().sum())
    mem_bytes = int(df.memory_usage(deep=True).sum())
    return {
        "rows": rows,
        "cols": cols,
        "columns": df.columns.tolist(),
        "dtypes_count": dtypes,
        "missing_cells": missing,
        "memory_bytes": mem_bytes,
    }


def data_dictionary(df: pd.DataFrame) -> pd.DataFrame:
    """Diccionario de datos (columna, tipo, no-nulos, únicos, %nulos, muestra)."""
    out = []
    n = len(df)
    for c in df.columns:
        s = df[c]
        dtype = str(s.dtype)
        non_null = int(s.notna().sum())
        nunique = int(s.nunique(dropna=True))
        missing = int(s.isna().sum())
        missing_pct = (missing / n) * 100 if n > 0 else 0.0
        sample_vals = s.dropna().astype(str).head(3).tolist() if non_null > 0 else []
        row: Dict[str, object] = {
            "column": c,
            "dtype": dtype,
            "non_null": non_null,
            "nunique": nunique,
            "missing": missing,
            "missing_pct": round(missing_pct, 2),
            "sample": " | ".join(sample_vals),
        }
        if np.issubdtype(s.dtype, np.number):
            row["min"] = float(np.nanmin(s)) if non_null > 0 else None
            row["max"] = float(np.nanmax(s)) if non_null > 0 else None
            row["mean"] = float(np.nanmean(s)) if non_null > 0 else None
        out.append(row)
    dd = pd.DataFrame(out)
    return dd


def save_dictionary_csv(dd: pd.DataFrame, path: str) -> None:
    dd.to_csv(path, index=False, encoding="utf-8")


def quality_flags(df: pd.DataFrame, dd: pd.DataFrame) -> Dict[str, object]:
    """Flags simples de calidad: columnas constantes, alta ausencia, posibles IDs, duplicados."""
    n = len(df)
    high_missing_cols = dd.loc[dd["missing_pct"] > 30, "column"].tolist() if "missing_pct" in dd else []
    constant_cols = dd.loc[dd["nunique"] <= 1, "column"].tolist() if "nunique" in dd else []
    suspected_ids = dd.loc[dd["nunique"] >= max(2, int(n * 0.9)), "column"].tolist() if n > 0 and "nunique" in dd else []
    dup_rows = int(df.duplicated().sum())
    return {
        "rows": n,
        "high_missing_cols": high_missing_cols,
        "constant_cols": constant_cols,
        "suspected_id_like": suspected_ids,
        "duplicate_rows": dup_rows,
    }


# ------------------------------
# Gráficos
# ------------------------------
def plot_missing_bar(df: pd.DataFrame, outfile: str) -> None:
    miss_pct = df.isna().mean().sort_values(ascending=True) * 100.0
    if len(miss_pct) == 0:
        return
    fig, ax = plt.subplots(figsize=(10, max(4, len(miss_pct) * 0.25)))
    ax.barh(miss_pct.index, miss_pct.values)
    ax.set_xlabel("% de valores perdidos")
    ax.set_ylabel("Variables")
    ax.set_title("Porcentaje de valores perdidos por variable")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    ensure_dir(os.path.dirname(outfile))
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _grid_size(k: int) -> tuple[int, int]:
    if k <= 0:
        return (1, 1)
    cols = int(np.ceil(np.sqrt(k)))
    rows = int(np.ceil(k / cols))
    return rows, cols


def plot_histograms(df: pd.DataFrame, outdir: str, max_cols: int = 12) -> None:
    num = df.select_dtypes(include=[np.number]).copy()
    if num.shape[1] == 0:
        return
    cols = num.columns[:max_cols]
    r, c = _grid_size(len(cols))
    fig, axes = plt.subplots(r, c, figsize=(4 * c + 2, 3.2 * r + 2))
    axes = np.array(axes).reshape(-1)
    for ax, col in zip(axes, cols):
        ax.hist(num[col].dropna(), bins=30)
        ax.set_title(col)
        ax.grid(True, linestyle="--", alpha=0.3)
    for ax in axes[len(cols):]:
        ax.axis("off")
    ensure_dir(outdir)
    fig.suptitle("Histogramas variables numéricas", y=0.995)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "histograms.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_boxplots(df: pd.DataFrame, outdir: str, max_cols: int = 8) -> None:
    num = df.select_dtypes(include=[np.number]).copy()
    if num.shape[1] == 0:
        return
    cols = num.columns[:max_cols]
    r, c = _grid_size(len(cols))
    fig, axes = plt.subplots(r, c, figsize=(4 * c + 2, 3.2 * r + 2))
    axes = np.array(axes).reshape(-1)
    for ax, col in zip(axes, cols):
        ax.boxplot(num[col].dropna(), vert=True)
        ax.set_title(col)
        ax.grid(True, linestyle="--", alpha=0.3)
    for ax in axes[len(cols):]:
        ax.axis("off")
    ensure_dir(outdir)
    fig.suptitle("Boxplots variables numéricas", y=0.995)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "boxplots.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_correlation(df: pd.DataFrame, outfile: str) -> None:
    num = df.select_dtypes(include=[np.number])
    if num.shape[1] < 2:
        return
    corr = num.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(1.2 * len(corr.columns) + 2, 1.2 * len(corr.columns) + 2))
    im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)
    ax.set_yticklabels(corr.columns)
    ax.set_title("Matriz de correlación (numéricas)")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ensure_dir(os.path.dirname(outfile))
    fig.tight_layout()
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="CRISP-DM · Data Understanding (VS Code + Git)"
    )
    ap.add_argument("--input", required=True, help="Ruta al archivo (.xlsx/.csv)")
    ap.add_argument("--sep", default="auto", help="Separador CSV (auto, ',', ';', '\\t', '|')")
    ap.add_argument("--sheet", default=None, help="Hoja Excel (índice o nombre)")
    ap.add_argument("--max-hist", type=int, default=12, help="Máx. columnas numéricas para histogramas")
    ap.add_argument("--max-box", type=int, default=8, help="Máx. columnas numéricas para boxplots")
    return ap.parse_args()


def main() -> None:
    logger = get_logger()
    args = parse_args()

    # Carpetas de salida
    ensure_dir("reports")
    ensure_dir("reports/figures")
    ensure_dir("data/interim")

    # Lectura de datos
    sheet: Optional[Union[int, str]] = None
    if args.sheet is not None:
        try:
            sheet = int(args.sheet)
        except ValueError:
            sheet = args.sheet

    logger.info(f"Leyendo datos: {args.input}")
    df = read_any(args.input, sep=args.sep, sheet=sheet)

    # 🔹 Limpieza de columnas Unnamed
    if all(df.columns.str.contains("^Unnamed")):
        logger.warning("Todas las columnas fueron 'Unnamed'. Revisa el header en read_excel.")
    else:
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Copia con nombres de columnas normalizados y muestra
    df_cols_norm = df.copy()
    df_cols_norm.columns = [str(c).strip().replace(" ", "_") for c in df.columns]
    df_cols_norm.head(100).to_csv("data/interim/sample_head.csv", index=False, encoding="utf-8")

    # Overview
    ov = data_overview(df_cols_norm)
    logger.info(f"Dimensiones: {ov['rows']} filas × {ov['cols']} columnas")
    logger.info(f"Primeras columnas: {ov['columns'][:5]}")

    # Diccionario de datos
    if ov["cols"] > 0:
        dd = data_dictionary(df_cols_norm)
        save_dictionary_csv(dd, "reports/data_dictionary.csv")
        dd.to_csv("data/interim/_data_dictionary_debug.csv", index=False, encoding="utf-8")

        # Flags de calidad
        flags = quality_flags(df_cols_norm, dd)
        with open("reports/quality_flags.json", "w", encoding="utf-8") as f:
            json.dump(flags, f, ensure_ascii=False, indent=2)
        logger.info(f"Flags de calidad: {flags}")

        # Gráficos
        logger.info("Generando gráficos...")
        plot_missing_bar(df_cols_norm, "reports/figures/missing_bar.png")
        plot_histograms(df_cols_norm, "reports/figures", max_cols=args.max_hist)
        plot_boxplots(df_cols_norm, "reports/figures", max_cols=args.max_box)
        plot_correlation(df_cols_norm, "reports/figures/corr_matrix.png")

        # Tablas de perfilado básico
        num = df_cols_norm.select_dtypes(include=[np.number])
        if num.shape[1] > 0:
            num.describe().to_csv("reports/numeric_summary.csv", encoding="utf-8")

        cat = df_cols_norm.select_dtypes(exclude=[np.number])
        for c in cat.columns:
            vc = cat[c].value_counts(dropna=False).head(20)
            vc.to_csv(f"reports/{c}_top20_value_counts.csv", encoding="utf-8")

    else:
        logger.error("No se detectaron columnas válidas en el archivo. Revisa el Excel y el header.")

    logger.info("Listo. Revisa carpetas 'reports' y 'reports/figures'.")


if __name__ == "__main__":
    main()
##fin