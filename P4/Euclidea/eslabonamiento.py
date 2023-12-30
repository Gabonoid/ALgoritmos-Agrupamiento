import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

MIN = 'MIN'
MAX = 'MAX'
MID = 'MID'


class Distancia():

    def __init__(self, primerIndice, segundoIndice, diccionario, tipo):
        global MIN, MAX, MID
        indices, combinaciones = Distancia._eslabon_indice(
            primerIndice, segundoIndice, diccionario, tipo)
        self.indices = indices
        self.distancia = combinaciones

    def _eslabon_indice(primerIndice, segundoIndice, diccionario, tipo):
        indices = []
        distancia = 0
        if tipo == 'MIN':
            distancia_menor = diccionario.get((0, 1))
            for i in range(len(primerIndice)):
                for j in range(len(segundoIndice)):
                    valor_i = primerIndice[i]
                    valor_j = segundoIndice[j]
                    combinacion_indices = tuple(sorted((valor_i, valor_j)))
                    valor_combionacion = diccionario.get(combinacion_indices)
                    distancia_menor = min(distancia_menor, valor_combionacion)

            combinacion = sorted(primerIndice + segundoIndice)
            indices = combinacion
            distancia = distancia_menor

        elif tipo == 'MID':
            promedio = 0
            for i in range(len(primerIndice)):
                for j in range(len(segundoIndice)):
                    valor_i = primerIndice[i]
                    valor_j = segundoIndice[j]
                    combinacion_indices = tuple(sorted((valor_i, valor_j)))
                    valor_combionacion = diccionario.get(combinacion_indices)
                    promedio += valor_combionacion
            combinacion = sorted(primerIndice + segundoIndice)
            indices = combinacion
            distancia = promedio / (len(primerIndice) * len(segundoIndice))

        elif tipo == 'MAX':
            distancia_mayor = diccionario.get((0, 1))
            for i in range(len(primerIndice)):
                for j in range(len(segundoIndice)):
                    valor_i = primerIndice[i]
                    valor_j = segundoIndice[j]
                    combinacion_indices = tuple(sorted((valor_i, valor_j)))
                    valor_combionacion = diccionario.get(combinacion_indices)
                    distancia_mayor = max(distancia_mayor, valor_combionacion)

            combinacion = sorted(primerIndice + segundoIndice)
            indices = combinacion
            distancia = distancia_mayor

        return indices, distancia

    @staticmethod
    def eslabonamiento(diccionario, tamanio_matriz, tipo):
        indices = [[i] for i in range(tamanio_matriz)]
        print(indices)

        while len(indices) > 1:
            distancias = []
            for i in range(len(indices)):
                for j in range(i+1, len(indices)):
                    indices_verticales = indices[i]
                    indices_horizontales = indices[j]
                    distancias.append(
                        Distancia(
                            primerIndice=indices_verticales,
                            segundoIndice=indices_horizontales,
                            diccionario=diccionario,
                            tipo=tipo
                        )
                    )

            ''' for distacia in distancias:
                print(distacia) '''

            distancia_menor = Distancia.distancia_menor(distancias)
            # print("\nEl menor fue", distancia_menor, '\n')

            indices_eliminar = distancia_menor.indices
            for int_eliminar in indices_eliminar:
                indices = [
                    lista for lista in indices if int_eliminar not in lista]

            indices.append(indices_eliminar)
            print(indices)

    def distancia_menor(distancias):
        menor = distancias[0]
        for distancia in distancias:
            if distancia.distancia < menor.distancia:
                menor = distancia
        return menor

    def __str__(self):
        return f'D{self.indices} = {self.distancia}'

def puntuacion_z(datos):
    tabla_z = []
    valor_promedios = promedios(datos)
    valor_desviacion_estandar = desviacion_estandar(datos, valor_promedios)
    for fila in datos:
        fila_z = []
        for i in range(len(fila)):
            fila_z.append((fila[i]-valor_promedios[i]) /
                          valor_desviacion_estandar[i])
        tabla_z.append(fila_z)

    return tabla_z


def desviacion_estandar(datos, promedios):
    sumaCuadradados = []
    for i in range(len(datos[0])):
        columna = [fila[i] for fila in datos]
        sumaCuadrado = 0
        for valor in columna:
            sumaCuadrado += (valor - promedios[i])**2
        varianza = sumaCuadrado/(len(columna)-1)
        sumaCuadradados.append(varianza**.5)
    return sumaCuadradados


def promedios(datos):
    promedios = []
    for i in range(len(datos[0])):
        promedio = sum([fila[i] for fila in datos])/len(datos)
        promedios.append(promedio)
    return promedios


def num_combinaciones(n):
    return n*(n-1)/2


def distacia_euclidiana(x, y):
    distacia = 0
    for i in range(len(x)):
        distacia += (x[i]-y[i])**2
    return distacia**.5


def diccionario_distancias(datos):
    diccionario = {}
    for i in range(len(datos)):
        for j in range(i+1, len(datos)):
            fila_uno = datos[i]
            fila_dos = datos[j]
            distancia = distacia_euclidiana(fila_uno, fila_dos)
            diccionario[(i, j)] = distancia
    return diccionario

def graficar_dendrograma(data, tipo):

    data = np.array(data)

    if tipo == 'MIN':
        linkage_matrix = linkage(data, 'single') # minimo
    elif tipo == 'MID':
        linkage_matrix = linkage(data, 'average') # promedio
    elif tipo == 'MAX':
        linkage_matrix = linkage(data, 'complete') # maximo

    dendrogram(linkage_matrix)
    plt.title(f'Dendrograma {tipo}')
    plt.yticks([]) # Elimina los valores del eje y
    plt.xlabel('Inidices')
    plt.show()
