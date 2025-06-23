'''Función para convertir los valores de SAR AlosPalsar a Power Backscatter '''

import ee

def dn_to_gamma_db (image):
    '''
    Convierte una imagen SAR con valores DN (Digital Numbers) a retrodispersión Gamma en decibelios (dB).

    Fórmula original de ALOS PALSAR:
        Gamma_dB = 10 * log10(DN^2) - 83.0

    Esta fórmula es equivalente a:
        Gamma_dB = 20 * log10(DN) - 83.0
        '''
    image_float = image.toFloat()
    gamma_db = image_float.select(['HH', 'HV']).log10().multiply(20).subtract(83.0).rename(['HH_dB', 'HV_dB'])
    return gamma_db

def db_to_gamma_pw (image_db):
    '''
    Convierte una imagen SAR con valores de gamma en dB (decibelios) a retrodispersión Gamma en power Backscatter - Potencia lineal (PW).

    Fórmula:
        Gamma_pw = 10^(0.1*Gamma_dB)
        '''
    bands = image_db.bandNames()
    pw_names = bands.map(lambda b: ee.String(b).replace('_dB', '_pw'))
    gamma_pw = ee.Image(10).pow(image_db.multiply(0.1))
    return gamma_pw.rename(pw_names)