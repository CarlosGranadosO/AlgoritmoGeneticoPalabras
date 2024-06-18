# AlgoritmoGeneticoPalabras
Este proyecto implementa un algoritmo genético para encontrar una palabra o frase objetivo a partir de una población inicial de cadenas de caracteres aleatorias.

## Descripción

Este proyecto utiliza un algoritmo genético para evolucionar una población de palabras aleatorias hasta que una de ellas coincide con una palabra o frase objetivo.

## Características

- Inicialización de una población de cadenas de caracteres aleatorias.
- Evaluación de la aptitud basada en la similitud con la palabra objetivo.
- Selección de individuos para la reproducción.
- Cruce  para combinar características de los padres.
- Mutación para introducir variabilidad.
- Iteración del proceso hasta encontrar la palabra objetivo.

## Instalación

1. Clona este repositorio en tu máquina local:

    bash
    git clone https://github.com/CarlosGranadosO/AlgoritmoGeneticoPalabras.git
    

2. Navega al directorio del proyecto:

    bash
    cd algoritmo-genetico-palabras
    

3. Instala las dependencias requeridas (si las hay):

    bash
    # Por ejemplo, si usas Python y tienes un requirements.txt
    pip install -r requirements.txt
    

## Uso

1. Abre el archivo de configuración y ajusta los parámetros según tus necesidades:

    python
    # configuración en config.py (por ejemplo)
    objetivo = "Hola Mundo"
    poblacionMax = 100
    mutacion = 0.01
    generaciones = 1000
    

2. Ejecuta el algoritmo:

    bash
    python algGen.py
    

3. Observa la evolución de la población en la consola hasta que se encuentre la palabra objetivo o se alcance el número máximo de generaciones.

## Ejemplo de Salida

