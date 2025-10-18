# Caracterización de NNA en Programas de Intervención en Trabajo Infantil - Grupo 4

## Estudiantes: Mariana Celis & Yuneidy Gutierrez

## CRISP-DM Fase 1: Business Understanding

---

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Problema y Contexto](#problema-y-contexto)
- [Objetivos](#objetivos)
- [Metodología](#metodología)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Resultados Esperados](#resultados-esperados)
- [Cronograma](#cronograma)
- [Equipo y Stakeholders](#equipo-y-stakeholders)

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

| Fase | Descripción | Entregable |
|------|-------------|-----------|
| **1. Business Understanding** | Definición de objetivos, problemas y oportunidades | Documento de contexto |
| **2. Data Understanding** | Exploración, análisis de calidad y estructura | Reporte EDA |
| **3. Data Preparation** | Limpieza, transformación y preparación | Dataset preparado |
| **4. Modeling** | MCA y clustering para identificar perfiles | 4 perfiles definidos |
| **5. Evaluation** | Validación, interpretación y recomendaciones | Reporte de hallazgos |
| **6. Deployment** | Implementación, monitoreo y sostenibilidad | Plan de acción |

### Técnicas Utilizadas

- **Análisis Exploratorio de Datos (EDA)**: Comprensión de distribuciones, valores faltantes, outliers
- **Análisis de Correspondencias Múltiples (MCA)**: Reducción dimensional para variables categóricas
- **K-Means Clustering**: Segmentación en perfiles homogéneos
- **Validación**: Silhouette Score, Davies-Bouldin Index, Chi-Square tests

---

## Estructura del Proyecto

### Archivos Principales

```
proyecto-nna/
├── README.md (este archivo)
├── Notebooks/
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
└── documentacion/
    ├── Business_Understanding.md
    └── Guia_Tecnica.md
```

### Dataset

- **Período**: 2015-2025
- **Registros**: 56,473 NNA
- **Variables originales**: 50+
- **Variables seleccionadas**: 19 (con ≥40% completitud)
- **Variables categóricas**: 16
- **Variables discretizadas**: 3

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
- 23,672 NNA
- Datos completos y seguimiento integral
- Tasa de desvinculación: 77.3%
- Estratos bajos, mayoría colombianos

#### Perfil 2: Registro Administrativo Incompleto (35.5%)
- 20,065 NNA
- Problema sistémico de calidad de datos
- Alta tasa de desvinculación (83.6%) a pesar de incompletitud
- Requiere intervención en sistemas de registro

#### Perfil 3: Seguimiento Inconcluso (8.3%)
- 4,661 NNA
- Alto riesgo
- 57.6% sin resultado final documentado
- Posible abandono o pérdida de contacto

#### Perfil 4: Casos Sin Cierre Documentado (14.3%)
- 8,075 NNA
- 100% sin resultado de desvinculación
- Posibles casos activos o sin cierre administrativo

### Indicadores Clave de Desempeño (KPIs)

| Indicador | Valor | Meta | Estado |
|-----------|-------|------|--------|
| Completitud de Datos | 66.2% | ≥90% | Alerta |
| Tasa Desvinculación Exitosa | 75.8% | ≥80% | Satisfactorio |
| Tasa Cierre Administrativo | 54.5% | ≥95% | Crítico |
| Seguimiento Completo (P1) | 41.9% | ≥60% | Alerta |
| Casos en Riesgo (P3) | 8.3% | ≤5% | Alerta |

---

## Cronograma

| Fase | Duración | Estado |
|------|----------|--------|
| Business Understanding | 0.5 semana | ✓ Completado |
| Data Understanding (EDA) | 0.5 semanas | ✓ Completado |
| Data Preparation | 0.5 semanas | ✓ Completado |
| Modeling (MCA + Clustering) | 0.5 semanas | ✓ Completado |
| Evaluation & Interpretation | 0.5 semanas | ✓ Completado |
| Deployment & Documentation | 0.5 semanas | ✓ Completado |
| **TOTAL** | **3 semanas** | ✓ **COMPLETADO** |


---

## Uso del Proyecto

### Requisitos Técnicos

- Python 3.8+
- Bibliotecas: pandas, numpy, scikit-learn, prince, matplotlib, seaborn
- Google Colab o Jupyter Notebook
- Almacenamiento: Google Drive (mínimo 5GB)

### Instalación

```bash
# Clonar repositorio
git clone <url-del-repositorio>

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar notebooks en orden (01 a 04)
```

### Estructura de Ejecución

1. **Notebook 1**: Data Understanding - Exploración inicial (EDA)
2. **Notebook 2**: Data Preparation - Limpieza y transformación
3. **Notebook 3**: Modeling - MCA y clustering
4. **Notebook 4**: Evaluation & Deployment - Interpretación y recomendaciones

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

### Consideraciones Éticas

- Anonimización completa de identidades
- Evitar etiquetado estigmatizante
- Enfoque basado en derechos del niño
- Transparencia en decisiones y algoritmos

---

## Referencias

### Metodología
- CRISP-DM: Industry Standard Process for Data Mining

### Técnicas Estadísticas
- Análisis de Correspondencias Múltiples (MCA)
- K-Means Clustering
- Chi-Square Testing
- Silhouette Analysis

---

## Autores y Contribuciones

**Proyecto completado con metodología CRISP-DM**

Para preguntas, sugerencias o reportar problemas, contactar al equipo de análisis de datos.

---

## Licencia

Este proyecto utiliza datos confidenciales de la organización. El uso está restringido a propósitos de análisis interno autorizado.

---

## Control de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2025 | Versión inicial completa |

---

**Última actualización**: 2025
**Estado**: Proyecto Completado
**Fase CRISP-DM**: 1-6 (Todas Completadas)
