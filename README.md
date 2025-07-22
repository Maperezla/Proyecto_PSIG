# Estimación de biomasa por tipo de cobertura en el Parque Nacional Natural Amacayacu

> Proyecto postulado al **Premio MapBiomas Colombia - Categoría Académica**
>> Autoras: Perez Largo Maria Paula y Veloza Martinez Paula Rocio, estudiantes de maestría en Geomática, Universidad Nacional de Colombia
---

## Introducción y motivación

El presente investigación tiene por objetivo calcular la biomasa aérea asociada a los diferentes tipos de cobertura presentes en el Parque Nacional Natural Amacayacu, un ecosistema estratégico de la Amazonía colombiana. Para ello, se emplean imágenes satelitales provenientes de sensores ópticos y de radar, datos LiDAR del sensor GEDI y las coberturas de MapBiomas Colombia. Lo anterior, permite mejorar la comprensión espacial de la biomasa y su relación con las coberturas del territorio.

Este trabajo se postula al Premio MapBiomas Colombia debido a su meticuloso enfoque académico y su contribución metodológica al uso innovador de datos MapBiomas, potenciados mediante herramientas de inteligencia artificial (Random Forest) y técnicas de análisis espacial reproducibles en Python.

---

## Objetivos

### Objetivo general
Estimar la biomasa aérea por tipo de cobertura en el Parque Nacional Natural Amacayacu, integrando información a partir de imágenes satelitales (Sentinel-2, ALOS PALSAR, GEDI), Modelos Digitales de elevación y coberturas de MapBiomas Colombia, mediante algoritmos de aprendizaje automático.

### Objetivos específicos
1. Integrar imágenes de sensores ópticos, radar y LiDAR para caracterizar el entorno biofísico del PNN Amacayacu.
2. Relacionar las coberturas de MapBiomas con estimaciones de biomasa aérea.
3. Entrenar y validar modelos de regresión usando Random Forest para estimar biomasa por tipo de cobertura.
4. Generar mapas temáticos de biomasa y analizar su distribución por clase de cobertura y elevación.

---

## Tecnologías y librerías empleadas

- **Lenguaje principal:** Python 3.x  
- **Bibliotecas clave:**
  - `scikit-learn` – modelado Random Forest
  - `rasterio` – lectura y escritura de imágenes ráster
  - `geopandas` – manejo de información vectorial
  - `numpy`, `pandas`, `matplotlib` – análisis y visualización de datos
  - `earthengine-api` – acceso a imágenes desde Google Earth Engine (GEE)
 
---

## Estructura del repositorio

Amacayacu_Biomasa/


├── 📂data/ # Datos de entrada (raster, vector, GEDI, MapBiomas)

├── 📂notebooks/ # Jupyter Notebooks de análisis y modelado

     ├──📋AlosPalsar/ # Preprocesamiento imagenes ALOS PALSAR y función para calculo retrodispersión HH y HV
     ├──📋DEM/ # Cargar y visualizar Modelo Digital de Elevación
     ├──📋GEDI/ # Estimaciones de la densidad de biomasa aérea (AGBD) para el área de interes usando LiDAR
     ├──📋Mapbiomas/ # 

├── 📂src/ # Scripts en Python ejecutables por consola

├── 📂results/ # mapas, graficas (GeoTIFF, PNG, CSV)

├── 📂docs/ # Referencias

├── 📂presentation/ # diapostivas

├── README.md # Descripción del proyecto



