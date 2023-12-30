package com.uaem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Distancia {

  private List<Integer> indices;
  private double distancia;
  public static String max = "MAX";
  public static String mid = "MID";
  public static String min = "MIN";

  public Distancia(List<Integer> indices, double distancia) {
    this.indices = indices;
    this.distancia = distancia;
  }

  public Distancia(
    List<Integer> primerIndices,
    List<Integer> segundoIndices,
    Map<List<Integer>, Double> diccionario,
    String tipo
  ) {
    if (tipo.equals(Distancia.max)) {
      double distanciaMayor = diccionario.get(Arrays.asList(0, 1));

      for (int i = 0; i < primerIndices.size(); i++) {
        for (int j = 0; j < segundoIndices.size(); j++) {
          int valorI = primerIndices.get(i);
          int valorJ = segundoIndices.get(j);

          List<Integer> combinacionIndices = new ArrayList<Integer>();
          combinacionIndices.add(valorI);
          combinacionIndices.add(valorJ);
          Collections.sort(combinacionIndices);

          double valorCombinacion = diccionario.get(combinacionIndices);

          distanciaMayor =
            (valorCombinacion > distanciaMayor)
              ? valorCombinacion
              : distanciaMayor;
        }
      }

      List<Integer> combinacion = new ArrayList<Integer>();

      combinacion.addAll(primerIndices);
      combinacion.addAll(segundoIndices);

      Collections.sort(combinacion);
      this.indices = combinacion;
      this.distancia = distanciaMayor;
    } else if (tipo.equals(Distancia.mid)) {
      double promedio = 0;

      for (int i = 0; i < primerIndices.size(); i++) {
        for (int j = 0; j < segundoIndices.size(); j++) {
          int valorI = primerIndices.get(i);
          int valorJ = segundoIndices.get(j);

          List<Integer> combinacionIndices = new ArrayList<Integer>();
          combinacionIndices.add(valorI);
          combinacionIndices.add(valorJ);
          Collections.sort(combinacionIndices);

          promedio += diccionario.get(combinacionIndices);
        }
      }

      List<Integer> combinacion = new ArrayList<Integer>();

      combinacion.addAll(primerIndices);
      combinacion.addAll(segundoIndices);

      Collections.sort(combinacion);
      this.indices = combinacion;
      this.distancia =
        promedio / (primerIndices.size() * segundoIndices.size());
    } else if (tipo.equals(Distancia.min)) {
      double distanciaMenor = diccionario.get(Arrays.asList(0, 1));

      for (int i = 0; i < primerIndices.size(); i++) {
        for (int j = 0; j < segundoIndices.size(); j++) {
          int valorI = primerIndices.get(i);
          int valorJ = segundoIndices.get(j);

          List<Integer> combinacionIndices = new ArrayList<Integer>();
          combinacionIndices.add(valorI);
          combinacionIndices.add(valorJ);
          Collections.sort(combinacionIndices);

          double valorCombinacion = diccionario.get(combinacionIndices);

          distanciaMenor =
            (valorCombinacion < distanciaMenor)
              ? valorCombinacion
              : distanciaMenor;
        }
      }

      List<Integer> combinacion = new ArrayList<Integer>();

      combinacion.addAll(primerIndices);
      combinacion.addAll(segundoIndices);

      Collections.sort(combinacion);
      this.indices = combinacion;
      this.distancia = distanciaMenor;
    }
  }

  //   Propio
  public static Distancia distanciaMenor(List<Distancia> distancias) {
    Distancia menor = distancias.get(0);
    for (Distancia distancia : distancias) {
      if (distancia.getDistancia() < menor.getDistancia()) {
        menor = distancia;
      }
    }
    return menor;
  }

  public static void eslabonamiento(
    Map<List<Integer>, Double> diccionario,
    int tamanioMatriz,
    String tipo
  ) {
    List<List<Integer>> indices = new ArrayList<List<Integer>>();
    for (int i = 0; i < tamanioMatriz; i++) {
      indices.add(Arrays.asList(i));
    }
    System.out.println(indices);

    while (indices.size() > 1) {
      List<Distancia> distancias = new ArrayList<Distancia>();
      for (int i = 0; i < indices.size(); i++) {
        for (int j = i + 1; j < indices.size(); j++) {
          // Capturando los indices
          List<Integer> IndicesVerticales = indices.get(i);
          List<Integer> IndicesHorizontales = indices.get(j);

          distancias.add(
            new Distancia(
              IndicesVerticales,
              IndicesHorizontales,
              diccionario,
              tipo
            )
          );
        }
      }
      /* for (Distancia distancia : distancias) {
        System.out.print(distancia);
      } */
      Distancia distanciamenor = Distancia.distanciaMenor(distancias);

      // System.out.println("El menor fue " + distanciamenor);

      List<Integer> indicesEliminar = distanciamenor.getIndices();

      for (Integer intEliminar : indicesEliminar) {
        Iterator<List<Integer>> iterator = indices.iterator();
        while (iterator.hasNext()) {
          List<Integer> lista = iterator.next();
          if (lista.contains(intEliminar)) {
            iterator.remove();
          }
        }
      }
      indices.add(indicesEliminar);

      System.out.println(indices);
    }
  }

  public List<Integer> getIndices() {
    return indices;
  }

  public void setIndices(List<Integer> indices) {
    this.indices = indices;
  }

  public double getDistancia() {
    return distancia;
  }

  public void setDistancia(double distancia) {
    this.distancia = distancia;
  }

  @Override
  public String toString() {
    return "D" + indices + " = " + distancia;
  }
}
