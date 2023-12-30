package com.uaem.helpers;

import java.io.FileReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

public class Lectura {

  public static List<List<Double>> leer_csv(String path) {
    try (Reader reader = new FileReader(path);
             CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT)) {

            List<List<Double>> datosPorColumna = new ArrayList<>();
            int numColumnas = -1; // Número de columnas en el CSV

            for (CSVRecord csvRecord : csvParser) {
                if (numColumnas == -1) {
                    numColumnas = csvRecord.size();
                    // Inicializar listas para cada columna
                    for (int i = 0; i < numColumnas; i++) {
                        datosPorColumna.add(new ArrayList<>());
                    }
                }

                for (int i = 0; i < numColumnas; i++) {
                    String valor = csvRecord.get(i);
                    try {
                        double valorDouble = Double.parseDouble(valor);
                        datosPorColumna.get(i).add(valorDouble);
                    } catch (NumberFormatException e) {
                        System.err.println("Error al convertir el valor a double: " + valor);
                    }
                }
            }

            return datosPorColumna;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
  }
}
