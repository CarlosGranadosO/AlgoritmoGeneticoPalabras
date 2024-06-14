import random
import string

# Parámetros del algoritmo genético
objetivo = "Algoritmo Genetico" #la frase que queremos encontrar
poblacionMax = 200 #el tamaño de la poblacion
mutacion = 0.01 #la probabilidad de mutacion de cada caracter
generaciones = 1000 #el numero maximo de generaciones

# Rand individuo crea una cadena aleatoria de la longitud especificada
def randInd(length):#recivimos el lenght de la palabra objetivo
    return ''.join(random.choice(string.ascii_letters + ' ') for _ in range(length))#armamos al individuo concatenando letras rand + ''

# Evalua cuántos caracteres coinciden con la frase objetivo
def calificar(individuo):#individual= el sujeto en cuestion cuando se sortee
    #regresaremos la suma  
    # comparando los strings iterables (objetivo e individuo "caracter x caracter")
    #si la tupla correspondiente de obketivo e individuo es == se hace un +1
    return sum(1 for esperado, actual in zip(objetivo, individuo) if esperado == actual)

# Selección de dos padres por método de torneo
def elegirPadres(poblacion):
    posibilidades = 5                       # elegimos los 5 posibles individuos a competir
    padres = random.sample(poblacion, posibilidades)
    return max(padres, key=calificar), max(random.sample(poblacion, posibilidades), key=calificar) #devolvemos la tupla de 2 padres

# Cruzamiento de dos padres para crear un descendiente
def cruzar(p1, p2):
    puntoCorte = random.randint(0, len(p1) - 1)#se define el punte de corte donde se uniran
    return p1[:puntoCorte] + p2[puntoCorte:]#

#mutar al individuo
def mutar(individuo):
    mutado = []#declaramos al mutado
    for char in individuo: #recorremos los caracteres en el hijo
        if random.random() > mutacion:#si la mutacion no se da 
            mutado.append(char)       #se agrega el caracter normal
        else:                         #sino se agrega un ascii letter rand 
            mutado.append(random.choice(string.ascii_letters + ' '))
    
    mutado = ''.join(mutado) #los convertimos en un stringsito
    return mutado


# generamos la primera poblacion
poblacion = [randInd(len(objetivo)) for x in range(poblacionMax)]#genera un individuo(fun) mientras x<poblacionMax

# Algoritmo genético principal
for i in range(generaciones): #empezamos el ciclo hasta el maximo de generaciones posibles
    poblacion = sorted(poblacion, key=calificar, reverse=True)#usamos sort con la key esta sabrosa pa ordenar que wea

    if calificar(poblacion[0]) == len(objetivo):
        print(f"Frase encontrada: {poblacion[0]} en la generación {i}")
        break

    siguienteGeneracion = poblacion[:10]  # Agarramos los mejores 10 de la poblacion

    while len(siguienteGeneracion) < poblacionMax:
        p1, p2 = elegirPadres(poblacion)#sacamos a 2 papas extras de la poblacion aun asi se califican
        hijo = cruzar(p1, p2) #hacemos al hijo cruazon a los 2 papas 
        hijo = mutar(hijo) #mutamos al hijo
        siguienteGeneracion.append(hijo) #agramos al hijo mutado a la sig generacion

    poblacion = siguienteGeneracion #remplazamos la poblacion por esta nueva con los 10 mejores y los mutados

    # Salida de progreso
    print(f"Generación {i}: Mejor frase - {poblacion[0]} caracteres correctos {calificar(poblacion[0])}")

else:
    print("No se encontró la frase objetivo en el número máximo de generaciones")

