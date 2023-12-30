import pandas as pd


def lectura_csv(path):
    datos = pd.read_csv(path, header=None)

    # Crear un DataFrame para las columnas que contienen solo 0 y 1
    variables_binarias = datos.loc[:, (datos.nunique() == 2) & (
        datos.max() == 1) & (datos.min() == 0)]
    # Eliminar las columnas de 0 y 1 del DataFrame original
    datos = datos.drop(columns=variables_binarias.columns)

    # Crear dos DataFrames separados para enteros y decimales
    variables_cuantitativas = datos.select_dtypes(include='int64')
    variables_cualitativas = datos.select_dtypes(include='float64')

    return variables_binarias.values.tolist(), variables_cuantitativas.values.tolist(), variables_cualitativas.values.tolist()
