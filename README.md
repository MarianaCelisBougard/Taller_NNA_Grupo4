# Caracterización de NNA en Programas de Intervención en Trabajo Infantil - Grupo 4

## Estudiantes: Mariana Celis, Yuneidy Gutierrez & Josue Pedraza

## CRISP-DM Fase 1: Business Understanding

# Caracterización de NNA en Programas de Intervención en Trabajo Infantil

**CRISP-DM Fase 1: Business Understanding**

---

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Problema y Contexto](#problema-y-contexto)
- [Objetivos](#objetivos)
- [Metodología](#metodología)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Resultados Esperados](#resultados-esperados)
- [Criterios de Éxito](#criterios-de-éxito)
- [Casos de Éxito](#casos-de-éxito)
- [Cronograma](#cronograma)
- [Equipo y Stakeholders](#equipo-y-stakeholders)
- [Impacto Esperado](#impacto-esperado)
- [Limitaciones y Consideraciones](#limitaciones-y-consideraciones)
- [Referencias](#referencias)

---

## Descripción del Proyecto

Este proyecto aplica la metodología **CRISP-DM** (Cross Industry Standard Process for Data Mining) para caracterizar y segmentar una población de 56,473 Niños, Niñas y Adolescentes (NNA) en situación de trabajo infantil, atendidos a través de programas de intervención social en Colombia durante el período 2015-2025.

El objetivo es identificar perfiles homogéneos de NNA que permitan mejorar la focalización de intervenciones, evaluar impacto diferenciado por grupo y optimizar la asignación de recursos.

---

## Problema y Contexto

### Problemática Identificada

La organización cuenta con un sistema de información extenso (56,473 registros), pero enfrenta desafíos críticos:

- **Falta de caracterización sistemática**: No existe clasificación unificada de los diferentes tipos de NNA según sus características demográficas, socioeconómicas y de proceso de intervención.

- **Calidad de datos inconsistente**: Completitud variable entre variables (rango 0-100%), con 35.5% de casos presentando registro administrativo incompleto.

- **Ausencia de segmentación**: No se conoce la heterogeneidad dentro de la población, limitando intervenciones personalizadas.

- **Débil evaluación de impacto**: Sin perfiles claros, no se puede evaluar efectividad diferenciada.

- **Ineficiencia operacional**: Asignación de recursos sin considerar vulnerabilidad o riesgo de abandono.

### Pregunta Central de Investigación

¿Existen perfiles homogéneos diferenciados de NNA que permitan mejorar la comprensión de la población, identificar grupos prioritarios y diseñar intervenciones más efectivas?

---

## Objetivos

### Objetivo General

Caracterizar y segmentar la población de NNA mediante análisis multivariado para identificar perfiles que permitan mejorar la efectividad y focalización de intervenciones.

### Objetivos Específicos

1. Explorar la estructura, calidad y limitaciones de los datos disponibles
2. Preparar y transformar datos para análisis multivariado asegurando consistencia
3. Identificar perfiles distintos mediante Análisis de Correspondencias Múltiples (MCA) y clustering
4. Interpretar y validar perfiles con características significativas
5. Generar recomendaciones estratégicas específicas por perfil
6. Establecer sistema de monitoreo continuo con KPIs

---

## Metodología

### CRISP-DM: 6 Fases

| Fase | Descripción | Entregable | Estado |
|------|-------------|-----------|--------|
| Business Understanding | Definición de objetivos y oportunidades | Documento de contexto | Completado |
| Data Understanding | Exploración, análisis de calidad | Reporte EDA | Completado |
| Data Preparation | Limpieza, transformación | Dataset preparado | Completado |
| Modeling | MCA y clustering | 4 perfiles definidos | Completado |
| Evaluation | Validación, interpretación | Reporte de hallazgos | Completado |
| Deployment | Implementación y monitoreo | Plan de acción | Completado |

### Técnicas Utilizadas

- **Análisis Exploratorio de Datos (EDA)**: Comprensión de distribuciones, valores faltantes, outliers
- **Análisis de Correspondencias Múltiples (MCA)**: Reducción dimensional para variables categóricas
- **K-Means Clustering**: Segmentación en perfiles homogéneos
- **Validación**: Silhouette Score, Davies-Bouldin Index, Chi-Square tests

---

## Estructura del Proyecto

```
proyecto-nna/
├── README.md
├── notebooks/
│   ├── 01_Data_Understanding_EDA.ipynb
│   ├── 02_Data_Preparation.ipynb
│   ├── 03_Modeling_MCA.ipynb
│   └── 04_Evaluation_Deployment.ipynb
├── datos/
│   ├── datos_filtrados.xlsx
│   ├── datos_mca_preparados.csv
│   └── datos_con_clusters_LIMPIO.csv
├── resultados/
│   ├── datos_finales_con_perfiles.csv
│   ├── kpis_programa.xlsx
│   ├── recomendaciones_estrategicas.txt
│   ├── resumen_ejecutivo.txt
│   ├── plan_accion_priorizado.xlsx
│   └── infografia_perfiles.png
└── docs/
    ├── Business_Understanding.md
    └── Guia_Tecnica.md
```

### Dataset

- **Período**: 2015-2025
- **Registros**: 56,473 NNA
- **Variables originales**: 115
- **Variables seleccionadas**: 28 (con >= 40% completitud)
---

## Criterios de Éxito

### Criterios Técnicos

| Criterio | Métrica | Meta | Resultado |
|----------|---------|------|-----------|
| Varianza explicada | Inercia acumulada 5 dims | >= 50% | 68.2% - CUMPLIDO |
| Calidad clustering | Silhouette Score | > 0.5 | 0.559 - CUMPLIDO |
| Separación clusters | Davies-Bouldin Index | < 1.0 | 0.773 - CUMPLIDO |
| Tamaño mínimo por perfil | N registros | >= 1,000 | Todos cumplen - CUMPLIDO |
| Diferenciación | Chi-Square p-value | < 0.05 | Cumplido - CUMPLIDO |
| Reproducibilidad | Random state | Determinístico | Implementado - CUMPLIDO |

**Resultado Final**: Todos los criterios técnicos alcanzados exitosamente

## Resultados Esperados

### Perfiles Identificados (4 Clusters)

#### Perfil 1: Intervención Exitosa Documentada (41.9%)

- **Población**: 23,672 NNA
- **Características**: Datos completos, seguimiento integral
- **Tasa de desvinculación**: 77.3%
- **Perfil sociodemográfico**: Estratos bajos, mayoría colombianos
- **Implicación**: Modelo a replicar en toda la organización

#### Perfil 2: Registro Administrativo Incompleto (35.5%)

- **Población**: 20,065 NNA
- **Características**: Problema sistémico de captura de datos
- **Tasa de desvinculación**: 83.6% (alta a pesar de incompletitud)
- **Brecha**: 100% sin información de edad y estrato
- **Implicación**: Requiere intervención urgente en sistemas

#### Perfil 3: Seguimiento Inconcluso (8.3%)

- **Población**: 4,661 NNA
- **Características**: Alto riesgo de abandono
- **Sin resultado final**: 57.6% de los casos
- **Riesgo**: Posible pérdida de contacto
- **Implicación**: Necesita alertas tempranas y retención

#### Perfil 4: Casos Sin Cierre Documentado (14.3%)

- **Población**: 8,075 NNA
- **Características**: Sin resultado de desvinculación
- **Estado**: Posibles casos activos o sin cierre administrativo
- **Implicación**: Protocolo de cierre obligatorio requerido

### Indicadores Clave de Desempeño (KPIs)

| Indicador | Valor Actual | Meta | Estado |
|-----------|-------------|------|--------|
| Completitud de Datos | 66.2% | >= 90% | Alerta |
| Tasa Desvinculación Exitosa | 75.8% | >= 80% | Satisfactorio |
| Tasa Cierre Administrativo | 54.5% | >= 95% | Crítico |
| Seguimiento Completo (P1) | 41.9% | >= 60% | Alerta |
| Casos en Riesgo (P3) | 8.3% | <= 5% | Alerta |

---

## Criterios de Éxito

### Criterios Técnicos

| Criterio | Métrica | Meta | Resultado |
|----------|---------|------|-----------|
| Varianza explicada | Inercia acumulada 5 dims | >= 50% | 68.2% - CUMPLIDO |
| Calidad clustering | Silhouette Score | > 0.5 | 0.559 - CUMPLIDO |
| Separación clusters | Davies-Bouldin Index | < 1.0 | 0.773 - CUMPLIDO |
| Tamaño mínimo por perfil | N registros | >= 1,000 | Todos cumplen - CUMPLIDO |
| Diferenciación | Chi-Square p-value | < 0.05 | Cumplido - CUMPLIDO |
| Reproducibilidad | Random state | Determinístico | Implementado - CUMPLIDO |

**Resultado Final**: Todos los criterios técnicos alcanzados exitosamente

---

## Cronograma

| Fase | Duración | Estado |
|------|----------|--------|
| Business Understanding | 0.5 semana | Completado |
| Data Understanding (EDA) | 0.5 semanas | Completado |
| Data Preparation | 0.5 semanas | Completado |
| Modeling (MCA + Clustering) | 0.5 semanas | Completado |
| Evaluation & Interpretation | 0.5 semanas | Completado |
| Deployment & Documentation | 0.5 semanas | Completado |
| **TOTAL** | **3 semanas** | **COMPLETADO** |


---

## Limitaciones y Consideraciones

### Limitaciones Conocidas

- Completitud variable de datos (0-100% entre variables)
- Sobrerrepresentación de años recientes (2020-2025)
- Concentración geográfica en Bogotá
- Información retrospectiva con posibles sesgos de registro

### Supuestos del Análisis

- Los datos registrados reflejan validamente la realidad de cada NNA
- Las variables disponibles capturan suficientemente la heterogeneidad
- Los perfiles serán estables por al menos 12 meses
- La organización tiene capacidad para implementar recomendaciones


### Metodología

- CRISP-DM: Industry Standard Process for Data Mining

### Técnicas Estadísticas

- Análisis de Correspondencias Múltiples (MCA)
- K-Means Clustering
- Chi-Square Testing
- Silhouette Analysis

---



**Última actualización**: 2025

**Proyecto**: COMPLETADO - Todas las fases CRISP-DM implementadas
