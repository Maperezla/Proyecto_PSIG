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

├── 📂notebooks/ # Cada notebook aborda una fase específica del procesamiento de datos geoespaciales, desde la descarga y preprocesamiento de imágenes                           satelitales hasta la creación de modelos predictivos y la estimación de biomasa.


     ├──📋AlosPalsar/ # Preprocesamiento imagenes ALOS PALSAR y función para calculo retrodispersión HH y HV. 
                       Aquí se encontrara el código para cargar y procesar estas imágenes de radar, además de una función específica para el cálculo de la                          retrodispersión en polarizaciones HH y HV.Esto es crucial para el análisis de la estructura y el contenido de la vegetación, así como                        para la detección de cambios en la superficie terrestre.
     
     ├──📋DEM/ # Cargar y visualizar Modelo Digital de Elevación. 
                       Manipular y representar datos de elevación, que son fundamentales para una gran variedad de análisis geomáticos, desde                                       el cálculo de pendientes y orientaciones hasta la corrección topográfica de imágenes.
     
     ├──📋GEDI/ # Estimaciones de la densidad de biomasa aérea (AGBD) para el área de interes usando LiDAR. 
                       Estos scripts te permitirán procesar y analizar los datos de forma de onda de GEDI para obtener valiosas métricas de biomasa para tu                         área de interés, lo cual es vital para estudios de carbono y ecología forestal.
     
     ├──📋Mapbiomas/ # Recorte y visualización de MapBiomas Colombia para el área de interes. 
                      Permite adaptar los conjuntos de datos de uso y cobertura del suelo de MapBiomas al área de estudio específica, facilitando análisis                         de cambio en el paisaje y caracterización de ecosistemas.
     
     ├──📋ModelRF/ # Modelo de regresión Random Forest. 
                     Permite entrenar y evaluar modelos predictivos utilizando variables geoespaciales
     
     ├──📋Resampleo/ # Resampleo de todas las imagenes a partir de los metadatos del Modelo Digital de Elevación (EPSG:9377, resolución espacial: 30 metros)
                      Uniformidad espacial de los datos, ajustando la resolución y el sistema de coordenadas de todas las imágenes a partir de los metadatos                       de tu Modelo Digital de Elevación (específicamente, **EPSG:9377 con una resolución espacial de 30 metros**). Esto es fundamental para                        la integración de múltiples fuentes de datos.
     
     ├──📋Sentinel2/ # Pre-procesamiento de imagenes Sentinel 2 y variables explicativas de modelo. 
                     Correcciones atmosféricas, calcuLo de índices de vegetación y extraer otras características espectrales útiles para análisis                                 posteriores y la alimentación de modelos machine learnin
     
     ├──📋TraininPoints/ # Exploración y extracción del centroide de los datos GEDI.
                     Puntos de entrenamiento para la calibración y validación de modelos de biomasa 
     
     ├──📋Unificacion_imagenes/ # Combinación de múltiples archivos raster. 
                     Apilar diferentes capas ráster, lo que es esencial para crear conjuntos de datos geoespaciales completos y unificados a partir de                            diversas fuentes.
     
     
├── 📂src/ # Scripts en Python ejecutables por consola.

      ├── 🛠️ SARFuction.py/ # Función para convertir los valores de SAR AlosPalsar a Power Backscatter
      
      ├── 🛠️ indices_sentinel2.py/ # Calcula los índices NDVI, EVI y BSI, y selecciona las bandas RED, NIR, SWIR1 y SWIR2. A partir de una imagen Sentinel-2                                       ya prefiltrada

├── 📂results/ # mapas, graficas (GeoTIFF, PNG, CSV)


├── 📂docs/ # Referencias

 
├── 📂presentation/ # diapositivas


├── README.md # Descripción del proyecto



