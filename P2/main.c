#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

// Función para leer un archivo CSV y convertirlo en una matriz de enteros
int **leer_archivo_csv(const char *path, int *numFilas, int *numColumnas)
{
    FILE *archivo = fopen(path, "r");
    if (archivo == NULL)
    {
        perror("Error al abrir el archivo");
        exit(EXIT_FAILURE);
    }

    // Contar el número de filas y columnas en el archivo CSV
    *numFilas = 0;
    *numColumnas = 0;

    char linea[1000]; // Supongamos que cada línea del archivo no excede los 1000 caracteres

    while (fgets(linea, sizeof(linea), archivo) != NULL)
    {
        (*numFilas)++;
        char *coma = strtok(linea, ",");
        int columnasEnFila = 0;
        while (coma != NULL)
        {
            columnasEnFila++;
            coma = strtok(NULL, ",");
        }
        if (columnasEnFila > *numColumnas)
        {
            *numColumnas = columnasEnFila;
        }
    }

    // Volver al principio del archivo
    fseek(archivo, 0, SEEK_SET);

    // Crear la matriz de enteros
    int **matriz = (int **)malloc(*numFilas * sizeof(int *));
    for (int i = 0; i < *numFilas; i++)
    {
        matriz[i] = (int *)malloc(*numColumnas * sizeof(int));
    }

    // Leer los valores y almacenarlos en la matriz de enteros
    for (int fila = 0; fila < *numFilas; fila++)
    {
        fgets(linea, sizeof(linea), archivo);
        char *coma = strtok(linea, ",");
        int columna = 0;
        while (coma != NULL)
        {
            matriz[fila][columna] = atoi(coma); // Convertir cadena a entero
            columna++;
            coma = strtok(NULL, ",");
        }
    }

    fclose(archivo);
    return matriz;
}

void imprimirYLibeMartriz(char ***matriz, int numFilas, int numColumnas)
{
    if (matriz != NULL)
    {
        // Imprimir la matriz
        for (int i = 0; i < numFilas; i++)
        {
            for (int j = 0; j < numColumnas; j++)
            {
                if (matriz[i][j] != NULL)
                {
                    printf("%s ", matriz[i][j]);
                }
                else
                {
                    printf("NULL ");
                }
            }
        }

        // Liberar la memoria cuando hayas terminado
        for (int i = 0; i < numFilas; i++)
        {
            for (int j = 0; j < numColumnas; j++)
            {
                if (matriz[i][j] != NULL)
                {
                    free(matriz[i][j]); // Liberar la memoria de la cadena de caracteres
                }
            }
            free(matriz[i]); // Liberar la memoria de las columnas
        }
        free(matriz); // Liberar la memoria de las filas
    }
}

int *factores_a(int **matriz, int numColumnas, int numFilas)
{
    int factor_a = 1;
    int contador_posicion = 0;
    int miArreglo[numFilas];

    for (int f = 0; f < numFilas; f++)
    {
        int contador_valores = 0; // Reiniciamos el contador por cada fila

        for (int a = 0; a < numColumnas; a++)
        {
            if (matriz[f][a] == factor_a)
            {
                contador_valores++;
            }
        }

        miArreglo[contador_posicion] = contador_valores;
        contador_posicion++;
    }

    // Lenar la matriz
    int nuevaMatriz[numFilas][numFilas];

    int cont = 0;

    for (int f = 0; f < numFilas; f++)
    {
        for (int a = 0; a < numFilas; a++)
        {
            if (f == a)
            {
                // Asigna un valor de miArreglo cuando los índices son iguales
                nuevaMatriz[f][a] = miArreglo[cont];
                cont++;
            }
            else
            {
                // Asigna 0 si los índices no son iguales
                nuevaMatriz[f][a] = 0;
            }
        }
    }

    int contador_a = 0;
    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < i; j++)
        {
            contador_a++;
        }
    }

    int *arreglo_A = (int *)malloc(contador_a * sizeof(int));

    if (arreglo_A == NULL)
    {
        // Manejo de errores si no se puede asignar memoria
        exit(1);
    }

    int contador_posicion_1 = 0;
    for (int i = 0; i < numFilas; i++)
    {

        for (int j = i + 1; j < numFilas; j++)
        {
            int contador_para_matriz = 0;
            // Accede a los valores de la matriz y muestra las agrupaciones
            int *valor1 = matriz[i];
            int *valor2 = matriz[j];

            // Imprime las coordenadas (i, j)
            // printf("Coordenadas (i, j): (%d, %d)\n", i  , j  );

            for (int k = 0; k < numColumnas; k++)
            {
                if (valor1[k] == 1 && valor2[k] == 1)
                {
                    contador_para_matriz++;
                }
            }
            nuevaMatriz[j][i] = contador_para_matriz;
            nuevaMatriz[i][j] = contador_para_matriz;
            arreglo_A[contador_posicion_1] = contador_para_matriz;
            contador_posicion_1++;
        }
    }

    printf("Factor A\n");

    // Imprime la nuevaMatriz para verificar
    for (int f = 0; f < numFilas; f++)
    {
        for (int c = 0; c < numFilas; c++)
        {
            printf("%3d ", nuevaMatriz[f][c]);
        }
        printf("\n");
    }

    return arreglo_A;
}

int *factores_c(int **matriz, int numColumnas, int numFilas)
{

    // Lenar la matriz
    int nuevaMatriz[numFilas][numFilas];

    int cont = 0;

    for (int f = 0; f < numFilas; f++)
    {
        for (int c = 0; c < numFilas; c++)
        {
            if (f == c)
            {
                // Asigna un valor de miArreglo cuando los índices son iguales
                nuevaMatriz[f][c] = 0;
                cont++;
            }
            else
            {
                // Asigna 0 si los índices no son iguales
                nuevaMatriz[f][c] = 0;
            }
        }
    }

    int contador_c = 0;
    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < i; j++)
        {
            contador_c++;
        }
    }

    int *arreglo_C = (int *)malloc(contador_c * sizeof(int));

    if (arreglo_C == NULL)
    {
        // Manejo de errores si no se puede asignar memoria
        exit(1);
    }

    int contador_posicion_1 = 0;
    for (int i = 0; i < numFilas; i++)
    {

        for (int j = i + 1; j < numFilas; j++)
        {
            int contador_matriz = 0;
            int contador_matriz_2 = 0;
            // Accede a los valores de la matriz y muestra las agrupaciones
            int *valor1 = matriz[i];
            int *valor2 = matriz[j];

            for (int k = 0; k < numColumnas; k++)
            {
                if (valor1[k] == 0 && valor2[k] == 1)
                {
                    contador_matriz++;
                }

                if (valor1[k] == 1 && valor2[k] == 0)
                {

                    contador_matriz_2++;
                }
            }
            nuevaMatriz[j][i] = contador_matriz;
            arreglo_C[contador_posicion_1] = contador_matriz;
            nuevaMatriz[i][j] = contador_matriz_2;
            contador_posicion_1++;
        }
    }

    printf("Factor C\n");

    // Imprime la nuevaMatriz para verificar
    for (int f = 0; f < numFilas; f++)
    {
        for (int c = 0; c < numFilas; c++)
        {
            printf("%3d ", nuevaMatriz[f][c]);
        }
        printf("\n");
    }

    return arreglo_C;
}

int *factores_b(int **matriz, int numColumnas, int numFilas)
{

    // Lenar la matriz
    int nuevaMatriz[numFilas][numFilas];

    int cont = 0;

    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < numFilas; j++)
        {
            if (i == j)
            {
                // Asigna un valor de miArreglo cuando los índices son iguales
                nuevaMatriz[i][j] = 0;
                cont++;
            }
            else
            {
                // Asigna 0 si los índices no son iguales
                nuevaMatriz[i][j] = 0;
            }
        }
    }

    int contador_b = 0;
    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < i; j++)
        {
            contador_b++;
        }
    }

    int *arreglo_B = (int *)malloc(contador_b * sizeof(int));

    if (arreglo_B == NULL)
    {
        // Manejo de errores si no se puede asignar memoria
        exit(1);
    }

    int contador_posicion_1 = 0;

    for (int i = 0; i < numFilas; i++)
    {

        for (int j = i + 1; j < numFilas; j++)
        {
            int contador_matriz = 0;
            int contador_matriz_2 = 0;
            // Accede a los valores de la matriz y muestra las agrupaciones
            int *valor1 = matriz[i];
            int *valor2 = matriz[j];

            for (int k = 0; k < numColumnas; k++)
            {
                if (valor1[k] == 1 && valor2[k] == 0)
                {
                    contador_matriz++;
                }

                if (valor1[k] == 0 && valor2[k] == 1)
                {

                    contador_matriz_2++;
                }
            }
            nuevaMatriz[j][i] = contador_matriz;
            arreglo_B[contador_posicion_1] = contador_matriz;
            nuevaMatriz[i][j] = contador_matriz_2;
            contador_posicion_1++;
        }
    }

    printf("Factor B\n");

    // Imprime la nuevaMatriz para verificar
    for (int f = 0; f < numFilas; f++)
    {
        for (int b = 0; b < numFilas; b++)
        {
            printf("%3d ", nuevaMatriz[f][b]);
        }
        printf("\n");
    }

    return arreglo_B;
}

int *factores_d(int **matriz, int numColumnas, int numFilas)
{

    int factor_d = 0;
    int contador_posicion = 0;
    int miArreglo[numFilas];

    for (int f = 0; f < numFilas; f++)
    {
        int contador_valores = 0; // Reiniciamos el contador por cada fila

        for (int d = 0; d < numColumnas; d++)
        {
            if (matriz[f][d] == factor_d)
            {
                contador_valores++;
            }
        }

        miArreglo[contador_posicion] = contador_valores;
        contador_posicion++;
    }

    int contador_d = 0;
    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < i; j++)
        {
            contador_d++;
        }
    }

    int *arreglo_D = (int *)malloc(contador_d * sizeof(int));

    if (arreglo_D == NULL)
    {
        // Manejo de errores si no se puede asignar memoria
        exit(1);
    }

    int contador_posicion_1 = 0;

    // Lenar la matriz
    int nuevaMatriz[numFilas][numFilas];

    int cont = 0;

    for (int f = 0; f < numFilas; f++)
    {
        for (int c = 0; c < numFilas; c++)
        {
            if (f == c)
            {
                // Asigna un valor de miArreglo cuando los índices son iguales
                nuevaMatriz[f][c] = miArreglo[cont];
                cont++;
            }
            else
            {
                // Asigna 0 si los índices no son iguales
                nuevaMatriz[f][c] = 0;
            }
        }
    }

    for (int i = 0; i < numFilas; i++)
    {

        for (int j = i + 1; j < numFilas; j++)
        {
            int contador_para_matriz = 0;
            int contador_para_matriz_2 = 0;
            // Accede a los valores de la matriz y muestra las agrupaciones
            int *valor1 = matriz[i];
            int *valor2 = matriz[j];

            // Imprime las coordenadas (i, j)
            // printf("Coordenadas (i, j): (%d, %d)\n", i  , j  );

            for (int k = 0; k < numColumnas; k++)
            {
                if (valor1[k] == 0 && valor2[k] == 0)
                {
                    contador_para_matriz++;
                }

                if (valor1[k] == 0 && valor2[k] == 0)
                {

                    contador_para_matriz_2++;
                }
            }
            nuevaMatriz[j][i] = contador_para_matriz;
            arreglo_D[contador_posicion_1] = contador_para_matriz;
            nuevaMatriz[i][j] = contador_para_matriz_2;
            contador_posicion_1++;
        }
    }

    printf("Factor D\n");

    // Imprime la nuevaMatriz para verificar
    for (int f = 0; f < numFilas; f++)
    {
        for (int c = 0; c < numFilas; c++)
        {
            printf("%3d ", nuevaMatriz[f][c]);
        }
        printf("\n");
    }

    return arreglo_D;
}

void sockal(int *factor_a, int *factor_c, int *factor_b, int *factor_d, int numFilas)
{
    int contador = 0;

    // Declarar e inicializar una matriz para almacenar los valores Jaccard
    float nuevaMatriz[numFilas][numFilas];

    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < numFilas; j++)
        {
            if (i == j)
            {
                // Establecer ceros en la diagonal principal
                nuevaMatriz[i][j] = 0;
            }
            else if (j > i)
            {
                // Calcular Jaccard solo por encima de la diagonal principal
                printf("D[%d,%d] = a : %d, b : %d, c : %d, d : %d\n", i+1, j+1, factor_a[contador], factor_c[contador], factor_b[contador], factor_d[contador]);

                float sockal = (float)(factor_a[contador] + factor_d[contador]) / (factor_a[contador] + factor_c[contador] + factor_b[contador] + factor_d[contador]);

                nuevaMatriz[i][j] = sockal;

                contador++;
            }
            else
            {
                // Usar simetría para las posiciones por debajo de la diagonal principal
                nuevaMatriz[i][j] = nuevaMatriz[j][i];
            }
        }
    }

    // Imprimir los valores debajo de la diagonal principal
    printf("Matriz Sockal:\n");
    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < numFilas; j++)
        {
            if (j < i)
            {
                printf("%.2f ", nuevaMatriz[i][j]);
            }
            else
            {
                printf("%.2f ", nuevaMatriz[j][i]); // Usar simetría para las posiciones por encima de la diagonal
            }
        }
        printf("\n");
    }
}

void jaccard(int *factor_a, int *factor_c, int *factor_b, int *factor_d, int numFilas)
{
    int contador = 0;

    // Declarar e inicializar una matriz para almacenar los valores Jaccard
    float nuevaMatriz[numFilas][numFilas];

    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < numFilas; j++)
        {
            if (i == j)
            {
                // Establecer ceros en la diagonal principal
                nuevaMatriz[i][j] = 0;
            }
            else if (j > i)
            {
                // Calcular Jaccard solo por encima de la diagonal principal
                printf("D[%d,%d] = a : %d, b : %d, c : %d, d : %d\n", i+1, j+1, factor_a[contador], factor_c[contador], factor_b[contador], factor_d[contador]);

                float Jaccard = (float)(factor_a[contador]) / (factor_a[contador] + factor_c[contador] + factor_b[contador]);

                nuevaMatriz[i][j] = Jaccard;
                contador++;
            }
            else
            {

                nuevaMatriz[i][j] = nuevaMatriz[j][i];
            }
        }
    }

    // Imprimir los valores debajo de la diagonal principal
    printf("Matriz Jaccard:\n");
    for (int i = 0; i < numFilas; i++)
    {
        for (int j = 0; j < numFilas; j++)
        {
            if (j < i)
            {
                printf("%.2f ", nuevaMatriz[i][j]);
            }
            else
            {
                printf("%.2f ", nuevaMatriz[j][i]); // Usar simetría para las posiciones por encima de la diagonal
            }
        }
        printf("\n");
    }
}

int main()
{
    const char *path = "C:\\Users\\Lapnoid\\Documents\\datos.csv";
    int numFilas, numColumnas;

    char ***matriz = leer_archivo_csv(path, &numFilas, &numColumnas);

    int *factor_a = factores_a(matriz, numColumnas, numFilas);

    int *factor_b = factores_b(matriz, numColumnas, numFilas);

    int *factor_c = factores_c(matriz, numColumnas, numFilas);

    int *factor_d = factores_d(matriz, numColumnas, numFilas);

    sockal(factor_a, factor_c, factor_b, factor_d, numFilas);

    jaccard(factor_a, factor_c, factor_b, factor_d, numFilas);

    return 0;
}
