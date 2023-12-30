import pandas as pd

def leer_csv(path, is_header = None):
    data = pd.read_csv(path, header = is_header, encoding='utf-8')
    return data.values.tolist()

def guardar_csv(path, data, header = None):
    data = pd.DataFrame(data)
    data.to_csv(path, header = header, index = False)