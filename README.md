
## 1. Comprensión del Negocio (Business Understanding)

### Contexto general
El conjunto de datos corresponde a registros administrativos de atención a **niños, niñas y adolescentes (NNA)** en procesos de **prevención y erradicación del trabajo infantil**.  
El propósito institucional de estos registros es comprender los patrones y características de la población atendida, con el fin de orientar decisiones sobre **focalización, seguimiento y evaluación de resultados**.

Desde un enfoque estadístico, el proyecto busca **caracterizar e identificar grupos homogéneos** dentro de la base de datos a partir de variables sociodemográficas, territoriales y de intervención, utilizando **técnicas exploratorias y de clustering no supervisado**.

---

### Propósito analítico
Desarrollar un proceso de análisis estadístico siguiendo la metodología **CRISP-DM**, que permita:
- Evaluar la **calidad, estructura y completitud** de la información.
- Aplicar **técnicas de reducción de dimensionalidad (PCA)** y **agrupamiento (clustering)**.
- Generar **perfiles interpretables de NNA** con características similares según los registros institucionales.

---

### Alcance técnico
- El estudio se centra exclusivamente en la base anónima proporcionada (`BD` del archivo `base_datos_completa_NNA_TI_anon.xlsx`).
- Se abordará un **enfoque exploratorio y descriptivo**, no predictivo.
- Las conclusiones se enfocan en **patrones estadísticos**, evitando interpretaciones causales o personales.
- Se prioriza la **reproducibilidad del análisis** en Python mediante notebooks documentados.

---

### Relevancia técnica
El enfoque de **clustering** permite:
- Agrupar individuos con características semejantes.
- Resumir la información en un número reducido de **perfiles representativos**.
- Detectar patrones de atención y diferencias territoriales.
- Brindar una herramienta analítica reproducible para el estudio institucional de datos sociales.

---

## Objetivos del Proyecto

### Objetivo General
Identificar y describir **grupos homogéneos de niños, niñas y adolescentes (NNA)** registrados en los programas de intervención frente al trabajo infantil, mediante técnicas de **análisis exploratorio y clustering no supervisado**, siguiendo la metodología **CRISP-DM**, con el fin de aportar una caracterización técnica que apoye la comprensión de los datos institucionales.

---

### Objetivos Específicos

1. **Comprensión y evaluación de la base de datos:**  
   Analizar la estructura, variables y calidad de los registros, identificando valores faltantes, inconsistencias y patrones de diligenciamiento (por ejemplo, el uso de códigos 99999).

2. **Preparación y depuración de datos:**  
   Seleccionar, transformar, codificar y estandarizar las variables relevantes para asegurar su idoneidad en el proceso de clustering.

3. **Aplicación de técnicas estadísticas:**  
   Implementar reducción de dimensionalidad (**PCA**) y **análisis de agrupamiento** (K-Means y/o jerárquico) para descubrir grupos representativos dentro de la población analizada.

4. **Interpretación y análisis de resultados:**  
   Describir los clusters identificados mediante estadísticas descriptivas y visualizaciones, destacando las principales características de cada grupo.

5. **Conclusiones técnicas:**  
   Elaborar un informe con los hallazgos y recomendaciones orientadas a la mejora de la calidad del registro y a futuras aplicaciones analíticas dentro del contexto institucional.

---

## 2. Comprensión de los Datos (Data Understanding)

### Fuente de datos
El análisis se desarrolla a partir del archivo **`base_datos_completa_NNA_TI_anon.xlsx`**, el cual contiene dos hojas principales:

- **`variables`** → Diccionario con los nombres, descripción y codificación de las variables disponibles.  
- **`BD`** → Base de datos principal con los registros de niños, niñas y adolescentes vinculados a programas de intervención.

---

### Descripción inicial
La base cuenta con **más de 56.000 registros** que representan casos individuales de NNA.  
Incluye variables de tipo:

- **Sociodemográficas:** edad, sexo, localidad, entre otras.  
- **Territoriales:** red o entidad de atención, profesional asignado, etc.  
- **Intervención:** tipo de proceso, estado actual, resultados alcanzados.  
- **Fechas y seguimiento:** periodos de ingreso, desvinculación, o finalización.  

Los valores `99999` se utilizan para representar **datos faltantes o no aplicables**, por lo que serán tratados como valores ausentes (`NaN`) durante la limpieza.

---

### Propósito de esta fase
- Explorar la estructura general de los datos.  
- Determinar el número de variables y tipos (numéricas, categóricas, texto).  
- Analizar la distribución de los valores válidos y ausentes.  
- Detectar variables con baja completitud o posibles errores de codificación.  
- Identificar las variables con **potencial analítico** para el proceso de clustering.

---

### Actividades principales

1. **Carga y revisión inicial del dataset:**  
   - Lectura de ambas hojas (`variables`, `BD`).  
   - Visualización de las primeras filas, tipos de datos y tamaño.  

2. **Análisis de completitud:**  
   - Cálculo del porcentaje de valores válidos y de `99999` por variable.  
   - Identificación de las variables con más del 40% de información disponible.  

3. **Evaluación de distribución de datos:**  
   - Estadísticos descriptivos básicos (media, mediana, moda, desviación estándar).  
   - Conteo de categorías y detección de valores atípicos.  

4. **Análisis exploratorio visual:**  
   - Gráficos de distribución de edad, localidad, tipo de intervención y estado de desvinculación.  
   - Heatmap de completitud de variables.  

5. **Selección preliminar de variables candidatas:**  
   - Criterios: relevancia conceptual + completitud ≥ 40%.  
   - Exclusión temporal de campos con alta proporción de 99999 o texto libre no estructurado.

---

### Consideraciones técnicas
- Se reemplazarán los valores `99999` por `NaN` para su correcto manejo en Python.  
- Las variables categóricas serán tratadas mediante codificación numérica (One-Hot Encoding o Label Encoding).  
- Se mantendrá trazabilidad del proceso de limpieza (registro de transformaciones).  
- En caso de bases muy grandes, se podrá utilizar una **muestra aleatoria representativa** para las pruebas iniciales.  

---

### Entregables de esta fase
1. **Informe exploratorio inicial:** resumen estadístico y visual de las variables.  
2. **Tabla de completitud:** porcentaje de datos válidos por variable.  
3. **Lista de variables seleccionadas** para la fase de preparación y modelado.  
4. **Notebook reproducible (`01_data_understanding.ipynb`)** con todo el proceso documentado.  

---

### Próximo paso
Realizar el **análisis exploratorio y de completitud**, el cual incluirá:
- Tabla con porcentaje de valores válidos por variable.  
- Heatmap de completitud.  
- Primeras visualizaciones descriptivas sobre las características principales de la población analizada.  

Este análisis permitirá definir con precisión qué variables serán incluidas en la siguiente fase de **Preparación de Datos (Data Preparation)**, donde se abordará la limpieza, codificación y transformación necesarias para el modelado de *clustering*.

