package com.uaem;

import com.uaem.helpers.Lectura;
import java.util.List;
import java.util.Map;

public class Main {

  public static void main(String[] args) {
    String path = "C:\\Users\\Lapnoid\\Documents\\test.csv";

    List<List<Double>> datos = Lectura.leer_csv(path);

    List<List<Double>> datos_z = Estadistica.puntuacionZ(datos);

    int tamanio_datos = datos_z.get(0).size();

    // Genero todas las distancias posibles
    Map<List<Integer>, Double> diccionario = Estadistica.diccionarioDistancias(
      datos_z
    );

    Distancia.eslabonamiento(diccionario, tamanio_datos, Distancia.max);
  }
}
