import numpy as np


class Distancia():
    indices = []
    distancia = 0

    def __init__(self, indices, distancia):
        self.indices = indices
        self.distancia = distancia

    def __str__(self):
        return f"D{self.indices} = {self.distancia:.2f}"


class Relacion():
    indices = []
    a = 0
    b = 0
    c = 0
    d = 0

    def __init__(self, indices, a, b, c, d):
        self.indices = indices
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"D{self.indices} = a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}"


def distancia_dicotomica(datos):
    fac_a = factor_a(datos)
    fac_b = factor_b(datos)
    fac_c = factor_c(datos)
    fac_d = factor_d(datos)
    print("\nFactor A")
    print(fac_a)
    print("\nFactor B")
    print(fac_b)
    print("\nFactor C")
    print(fac_c)
    print("\nFactor D")
    print(fac_d)
    return fac_a, fac_b, fac_c, fac_d


def calc_relacion(a, b, c, d):
    tamanio = len(a)
    relaciones = []
    for i in range(0, tamanio):
        for j in range(i + 1, tamanio):
            num_a = int(a[j][i])
            num_b = int(b[j][i])
            num_c = int(c[j][i])
            num_d = int(d[j][i])
            relaciones.append(Relacion([i+1, j+1], num_a, num_b, num_c, num_d))
    return relaciones


def sockal(relaciones):

    distacias = []
    for relacion in relaciones:
        distancia = (relacion.a+relacion.d) / \
            (relacion.a+relacion.b+relacion.c+relacion.d)
        distacias.append(Distancia(relacion.indices, distancia))
    return distacias


def jaccard(relaciones):
    distacias = []
    for relacion in relaciones:
        distancia = (relacion.a) / (relacion.a+relacion.b+relacion.c)
        distacias.append(Distancia(relacion.indices, distancia))
    return distacias


def factor_a(datos):
    len_matriz = len(datos)
    matriz = np.zeros((len_matriz, len_matriz))
    for i in range(0, len_matriz):
        for j in range(0, len_matriz):
            fila_uno = datos[i]
            fila_dos = datos[j]
            a = 0
            for k in range(0, len(fila_uno)):
                if fila_uno[k] == 1 and fila_dos[k] == 1:
                    a += 1
            matriz[i][j] = a
    return matriz


def factor_b(datos):
    matriz = np.zeros((len(datos), len(datos)))
    for i in range(0, len(datos)):
        for j in range(i+1, len(datos)):
            fila_uno = datos[i]
            fila_dos = datos[j]
            b = 0
            for k in range(0, len(fila_uno)):
                if fila_uno[k] == 0 and fila_dos[k] == 1:
                    b += 1
            matriz[j][i] = b
    return matriz


def factor_c(datos):
    matriz = np.zeros((len(datos), len(datos)))
    for i in range(0, len(datos)):
        for j in range(i+1, len(datos)):
            fila_uno = datos[i]
            fila_dos = datos[j]
            c = 0
            for k in range(0, len(fila_uno)):
                if fila_uno[k] == 1 and fila_dos[k] == 0:
                    c += 1
            matriz[j][i] = c
    return matriz


def factor_d(datos):
    len_matriz = len(datos)
    matriz = np.zeros((len_matriz, len_matriz))
    for i in range(0, len_matriz):
        for j in range(0, len_matriz):
            fila_uno = datos[i]
            fila_dos = datos[j]
            d = 0
            for k in range(0, len(fila_uno)):
                if fila_uno[k] == 0 and fila_dos[k] == 0:
                    d += 1
            matriz[i][j] = d
    return matriz

def imprimir_lista(datos):
        for fila in datos:
            print(fila)