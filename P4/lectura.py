import pandas as pd

def leer_archivo(path):
    return pd.read_csv(path, header=None)

# Analizando los datos para saber que algoritmo usar
def tipo_algoritmo(df):
    if ((df.isin([0, 1])).all().all()): # Si todos los valores son 0 o 1
        return "FACTORES"
    elif df.shape[1] == 2 and df.applymap(lambda x: isinstance(x, int)).all().all(): # Si son dos columnas y son enteros
        return "EUCLIDEA"
    else: # Si tiene mas de dos columnas y tiene valores decimales, enteros y binarios
        return "GOWER"