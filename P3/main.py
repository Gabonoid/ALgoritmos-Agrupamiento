from helpers import lectura as rd
from helpers import helper as hp
import algoritmo as alg

binarias, cuantitativas, cualitativas = rd.lectura_csv(r'C:\Users\Lapnoid\OneDrive - Universidad Autónoma del Estado de México\UAEM\9no Semestre\Agrupamiento\Algoritmos\Algoritmo3_python\test.csv')
print('Binarias: ')
hp.mostra_array(binarias)
print('Cuantitativas: ')
hp.mostra_array(cuantitativas)
print('Cualitativas: ')
hp.mostra_array(cualitativas)

alg.distancias_variables_mixta(binarias, cuantitativas, cualitativas)
