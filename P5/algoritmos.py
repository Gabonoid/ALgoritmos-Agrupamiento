from helpers import lectura
import numpy as np


def distancia_mahalanobis(data, to_print=False, to_suppress=False, num_suppress=3):

    if to_suppress:
        np.set_printoptions(precision=num_suppress, suppress=True)

    data = np.array(data)
    centroides = calcular_centroides(data)
    distancias_ind = distancia_centroide(data, centroides)
    v_c, v_c_inv = varianza_covarianza(distancias_ind)
    ind_inv = distancia_por_inv(distancias_ind, v_c_inv)
    valores_distancia_final = distancia_final(distancias_ind, ind_inv)

    if to_print:
        print("Datos\n", data)
        print("Centroides\n", centroides)
        print('Distacias individuales\n', distancias_ind)
        print('Varianza y Covarianza\n', v_c)
        print('Varianza y Covarianza Inversa\n', v_c_inv)
        print('Distancia Por Inversa Covarianza\n', ind_inv)
        print('Matriz Mahalanobis\n', valores_distancia_final)

    return valores_distancia_final


def calcular_centroides(datos):
    centroides = []
    for i in range(len(datos[0])):
        centroides.append(np.mean([fila[i] for fila in datos]))
    return np.array(centroides)


def distancia_centroide(datos, centroides):
    distancias = []
    for fila in datos:
        distancia = [valor-centroide for valor,
                     centroide in zip(fila, centroides)]
        distancias.append(distancia)
    return np.array(distancias)


def varianza_covarianza(datos):
    v_c = (datos.T @ datos) / (len(datos)-1)
    v_c_inv = np.linalg.inv(v_c)
    return v_c, v_c_inv


def distancia_por_inv(matriz_distancias, matriz_inversa):
    return matriz_distancias @ matriz_inversa


def distancia_final(distancias_ind, ind_inv):
    return ind_inv @ distancias_ind.T
