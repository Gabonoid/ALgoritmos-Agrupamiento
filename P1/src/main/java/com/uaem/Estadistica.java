package com.uaem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Estadistica {

  static List<List<Double>> puntuacionZ(List<List<Double>> datos) {
    List<List<Double>> tabla_z = new ArrayList<>();

    for (List<Double> fila : datos) {
      double promedio_valor = promedio(fila);
      double desviacion_estandar = desviacionEstandar(fila, promedio_valor);

      List<Double> puntuaciones_z = new ArrayList<>();

      for (double valor : fila) {
        double puntuacion_z = (valor - promedio_valor) / desviacion_estandar;
        puntuaciones_z.add(puntuacion_z);
      }

      tabla_z.add(puntuaciones_z);
    }

    return tabla_z;
  }

  static double promedio(List<Double> datos) {
    double suma = 0;
    for (Double valor : datos) {
      suma += valor;
    }
    return suma / datos.size();
  }

  static int numCombinaciones(int n) {
    return ((n - 1) * n) / 2;
  }

  static double desviacionEstandar(List<Double> datos, double promedio) {
    double sumaCuadrados = 0.0;
    for (double valor : datos) {
      sumaCuadrados += Math.pow(valor - promedio, 2);
    }
    double varianza = sumaCuadrados / (datos.size() - 1);
    return Math.sqrt(varianza);
  }

  static double calcularDistaciaEuclidiana(List<Double> x, List<Double> y) {
    double distancia = 0;

    for (int i = 0; i < x.size(); i++) {
      double diferencia = x.get(i) - y.get(i);
      distancia += Math.pow(diferencia, 2);
    }

    return Math.sqrt(distancia);
  }

  static Map<List<Integer>, Double> diccionarioDistancias(
    List<List<Double>> datos
  ) {
    Map<List<Integer>, Double> diccionario = new HashMap<>();
    int n = datos.get(0).size();

    // Recorremos nuestras listas
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        List<Double> filaUno = new ArrayList<>();
        List<Double> filaDos = new ArrayList<>();

        for (List<Double> columna : datos) {
          filaUno.add(columna.get(i));
          filaDos.add(columna.get(j));
        }
        double distancia = calcularDistaciaEuclidiana(filaUno, filaDos);
        diccionario.put(Arrays.asList(i, j), distancia);
      }
    }
    return diccionario;
  }
}
