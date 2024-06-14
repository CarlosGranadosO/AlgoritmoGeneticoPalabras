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
def select_parents(poblacion):
    tournament_size = 5
    parents = random.sample(poblacion, tournament_size)
    return max(parents, key=calificar), max(random.sample(poblacion, tournament_size), key=calificar)

# Cruzamiento de dos padres para crear un descendiente
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

# Mutar un individuo
def mutar(individuo):
    mutado = ''.join(
        (char if random.random() > mutacion else random.choice(string.ascii_letters + ' '))
        for char in individuo
    )
    return mutado

# generamos la primera poblacion
poblacion = [randInd(len(objetivo)) for x in range(poblacionMax)]#genera un individuo(fun) mientras x<poblacionMax

# Algoritmo genético principal
for i in range(generaciones): #empezamos el ciclo hasta el maximo de generaciones posibles
    poblacion = sorted(poblacion, key=calificar, reverse=True)#usamos sort con la key esta sabrosa pa ordenar que wea

    if calificar(poblacion[0]) == len(objetivo):
        print(f"Frase encontrada: {poblacion[0]} en la generación {i}")
        break

    next_generation = poblacion[:10]  # Elitismo: mantener los mejores 10 individuos

    while len(next_generation) < poblacionMax:
        parent1, parent2 = select_parents(poblacion)
        child = crossover(parent1, parent2)
        child = mutar(child)
        next_generation.append(child)

    poblacion = next_generation

    # Salida de progreso
    print(f"Generación {i}: Mejor frase - {poblacion[0]} con aptitud {calificar(poblacion[0])}")

else:
    print("No se encontró la frase objetivo en el número máximo de generaciones")

