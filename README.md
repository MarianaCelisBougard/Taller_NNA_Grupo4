
# Business Understanding

### Objetivos del Negocio

El propósito del proyecto es **comprender las condiciones de vida y vulnerabilidad de NNA entre 0 y 18 años**, con especial énfasis en el **riesgo de trabajo infantil**.
La base permite identificar patrones relacionados con escolaridad, salud, nutrición y entorno familiar, y a partir de ello **aportar insumos para programas de protección y atención integral**.

### Situación Actual

* **Recursos disponibles**: Base de datos consolidada en formato `.xlsx` con variables cuantitativas y cualitativas; script en Python (`data_NNA.py`) para análisis exploratorio.
* **Supuestos**: Los datos fueron recolectados de manera estandarizada en campo; pueden existir valores faltantes o inconsistencias.
* **Limitaciones**: No todas las variables están completas; algunas categorías presentan alta cardinalidad y existen columnas sensibles que requieren anonimización.
* **Beneficio esperado**: Facilitar la toma de decisiones de políticas públicas sobre niñez y adolescencia en situación de riesgo, con base en evidencia empírica.

### Metas de Minería de Datos

* Generar un **perfil descriptivo** de la población encuestada.
* Identificar **variables críticas** (educación, salud, nutrición, entorno socioeconómico).
* Explorar **relaciones entre variables** (ej. municipio × punto de atención, motivo de gestión × servicio recibido).
* Producir **visualizaciones claras** que apoyen la comunicación de hallazgos.

---

# Data Understanding

### Recolección Inicial

* **Fuente**: Archivo `base_datos_completa_NNA_TI_anon.xlsx`.
* **Tamaño**: Miles de registros (NNA encuestados).
* **Cobertura**: Variables de edad, género, nivel educativo, pertenencia étnica, estado de salud, acceso a servicios, condiciones familiares, intervenciones recibidas, entre otras.

### Descripción de Datos

* **Columnas numéricas**: Edad, número de personas en el hogar, tiempos y costos de traslado, entre otros.
* **Columnas categóricas**: Nivel educativo, ocupación, estado civil de los cuidadores, tipo de zona de residencia, satisfacción con la atención recibida, etc.
* **Variables sensibles**: Datos de identificación y texto libre fueron eliminados o anonimizados mediante hashing o reemplazo de PII.

### Exploración de Datos

El script `data_NNA.py` produjo:

* **Diccionario de datos** (`reports/data_dictionary.csv`) con tipos, nulos, cardinalidad.
* **Indicadores de calidad** (`reports/quality_flags.json`), mostrando columnas casi constantes, alta cardinalidad y duplicados.
* **Tablas de frecuencias** por variable y por grupo temático (`demografía`, `territorial_acceso`, `motivo_gestion`, `experiencia_satisfaccion`).
* **Visualizaciones**:

  * Porcentaje de valores faltantes.
  * Histogramas y boxplots para variables numéricas.
  * Barras horizontales Top-N para variables categóricas clave.
  * Cruces como municipio × punto de atención, motivo × servicio, etc.

### Verificación de Calidad

* Se detectaron columnas con valores faltantes significativos.
* Algunas variables categóricas presentan alta cardinalidad (ej. observaciones libres).
* Existen registros duplicados en pequeña proporción.
* Se identificaron columnas candidatas a ser IDs únicos, útiles para seguimiento.


# Continuacion Plan del Proyecto (CRISP-DM)


## 3. Data Preparation

* **Selección de Datos**
  Conservar variables relevantes para caracterización (edad, escolaridad, zona de residencia, ocupación, salud, nutrición). Excluir columnas altamente sensibles o redundantes.

* **Limpieza de Datos**

  * Manejo de nulos (imputación o eliminación).
  * Homogeneización de categorías.
  * Eliminación de duplicados.
  * Anonimización aplicada (hash en campos sensibles).

* **Construcción de Datos**
  Crear atributos derivados como:

  * Índices de vulnerabilidad (combinando variables de educación, nutrición y zona).
  * Variables binarias (ej. riesgo escolar = sí/no).

* **Integración de Datos**
  Si existen múltiples bases, consolidarlas en un dataset unificado.

* **Formato de Datos**
  Preparar datasets balanceados y listos para modelado, con variables codificadas (one-hot encoding) para categóricas.

---

## 4. Modeling

* **Selección de Técnicas**

  * Modelos de clasificación supervisada (árboles de decisión, random forest, regresión logística) para identificar NNA en riesgo.
  * Clustering (k-means, clustering jerárquico) para agrupar perfiles de vulnerabilidad.

* **Generación de Diseño de Pruebas**
  Dividir dataset en entrenamiento (70%) y prueba (30%). Validación cruzada para asegurar robustez.

* **Construcción del Modelo**
  Entrenar modelos con parámetros iniciales y ajustar hiperparámetros.

* **Evaluación del Modelo**
  Medir desempeño con métricas: accuracy, recall, precision y AUC, priorizando sensibilidad (identificación de casos de riesgo).

---

## 5. Evaluation

* **Evaluación de Resultados**
  Validar que los hallazgos se alineen con los objetivos de negocio: identificación clara de factores de riesgo en NNA.

* **Revisión del Proceso**
  Confirmar que el pipeline desde la limpieza hasta el modelado es reproducible y documentado.

* **Determinación de Próximos Pasos**

  * Adoptar modelos que mejor predigan vulnerabilidad.
  * Preparar reportes comprensibles para actores institucionales.
  * Diseñar un piloto de implementación en campo.

---

## 6. Deployment

* **Plan de Despliegue**
  Implementar el modelo en un entorno controlado (ej. dashboard en Power BI o aplicación web).

* **Plan de Monitoreo y Mantenimiento**

  * Actualización periódica de la base con nuevos registros.
  * Reevaluación del modelo cada 6 meses.

* **Reporte Final**
  Generar documentos y presentaciones para tomadores de decisiones con visualizaciones y recomendaciones.

* **Revisión del Proyecto**
  Documentar la experiencia, limitaciones y oportunidades de mejora, dejando lineamientos para próximas fases.


Medical References:
1. None — DOI: file-DwHjtodAH5LMWABzQWmkri
