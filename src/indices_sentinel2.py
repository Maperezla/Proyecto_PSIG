# archivo: indices_sentinel2.py

import ee

def indices_sentinel2(sentinel2_img):
    """
    Calcula los índices NDVI, EVI y BSI, y selecciona las bandas RED, NIR, SWIR1 y SWIR2
    a partir de una imagen Sentinel-2 ya prefiltrada.

    Parámetros:
    - sentinel2_img (ee.Image): Imagen Sentinel-2 con bandas mínimas requeridas:
      B2 (BLUE), B4 (RED), B8 (NIR), B11 (SWIR1), B12 (SWIR2)

    Retorna:
    - ee.Image: Imagen combinada con NDVI, EVI, BSI, RED, NIR, SWIR1 y SWIR2
    """

    # --- NDVI ---
    ndvi = sentinel2_img.normalizedDifference(['B8', 'B4']).rename('NDVI')

    # --- EVI ---
    evi = sentinel2_img.expression(
        '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
            'NIR': sentinel2_img.select('B8'),
            'RED': sentinel2_img.select('B4'),
            'BLUE': sentinel2_img.select('B2')
        }).rename('EVI')

    # --- BSI ---
    bsi = sentinel2_img.expression(
        '((SWIR1 + RED) - (NIR + BLUE)) / ((SWIR1 + RED) + (NIR + BLUE))', {
            'SWIR1': sentinel2_img.select('B11'),
            'RED': sentinel2_img.select('B4'),
            'NIR': sentinel2_img.select('B8'),
            'BLUE': sentinel2_img.select('B2')
        }).rename('BSI')

    # --- Selección y renombre de bandas ---
    red = sentinel2_img.select('B4').rename('RED')
    nir = sentinel2_img.select('B8').rename('NIR')
    swir1 = sentinel2_img.select('B11').rename('SWIR1')
    swir2 = sentinel2_img.select('B12').rename('SWIR2')

    # --- Combinar ---
    resultado = ee.Image([ndvi, evi, bsi, red, nir, swir1, swir2])

    return resultado
