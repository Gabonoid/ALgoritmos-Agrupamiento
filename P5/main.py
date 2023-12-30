from helpers import lectura
import algoritmos as alg

data = lectura.leer_csv(r'C:\Users\Lapnoid\OneDrive - Universidad Autónoma del Estado de México\UAEM\9no Semestre\Agrupamiento\Algoritmos\Algoritmo5\data\test.csv')
distancias = alg.distancia_mahalanobis(data=data, to_print=True)

lectura.guardar_csv('distancias.csv', distancias)

