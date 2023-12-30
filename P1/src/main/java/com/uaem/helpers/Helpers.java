package com.uaem.helpers;

import java.util.List;
import java.util.Map;

public class Helpers {

  public static void mostrarArray(double[] datos) {
    for (int i = 0; i < datos.length; i++) {
      System.out.println(datos[i]);
    }
    System.out.println();
  }

  public static void mostrarTabla(List<List<Double>> datos) {
    for (List<Double> fila : datos) {
      for (Double valor : fila) {
        System.out.print(valor + "\t");
      }
      System.out.println();
    }
    System.out.println();
  }

  public static void mostrarMapa(Map<List<Integer>, Double> mapa) {
    for (Map.Entry<List<Integer>, Double> entry : mapa.entrySet()) {
      List<Integer> clave = entry.getKey();
      Double valor = entry.getValue();
      System.out.println("D" + clave + " = " + valor);
    }
    System.out.println();
  }

  public static void mostrarLista(List<Double> datos) {
    for (Double valor : datos) {
      System.out.println(valor);
    }
    System.out.println();
  }
}
