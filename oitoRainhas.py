from random import randint

#base subject to create population without repetitions
baseSubject = "000001010011100101110111"

#solution for test purposes
solution = "100000111011001110010101"

test = ["000001010011100101110111", "000001010011100101110111"]

def shuffle (amount, base):
    newSubject = base
    for i in range(0, amount):
        i1 = randint(0,7)*3
        i2 = randint(0,7)*3
        aux1 = base[i1:(i1+3)]
        aux2 = base[i2:(i2+3)]
        partialShuffle = base[:i1] + aux2 + base[(i1+3):]
        newSubject = partialShuffle[:i2] + aux1 + partialShuffle[(i2+3):]
    return newSubject

def initialPopulation (size, baseIndividual):
    population = [None] * size
    for i in range(0, size):
        population[i] = shuffle(200, baseSubject)
    return population

def individualFitness (subject):
    colisions = 0
    for i in range(0, 7):
        ind = i*3
        aux = subject[ind:(ind+3)]
        value1 = int(bin(int(aux, 2)),2)
        for e in range((i+1), 8):
            ind2 = e * 3
            aux2 = subject[ind2:(ind2 + 3)]
            value2 = int(bin(int(aux2, 2)), 2)
            distance = e - i
            if ((value1 + distance) == value2) or ((value1 - distance) == value2):
                colisions = colisions + 1
    return colisions

def averagePopulationFitness (population):
    fitness = 0
    for i in range(0, len(population)):
        fitness = fitness + (individualFitness(population[i]))
    fitness = fitness / (len(population) + 1)
    return fitness

def cutAndCrossfill (parent1, parent2, cut):
    child = parent1[:(cut*3)]
    for i in range(0, 24, 3):
        aux = True
        for e in range(0, cut*3, 3):
            if (parent2[i:(i+3)] == parent1[e:(e+3)]):
                aux = False
        if aux:
            child = child + (parent2[i:(i+3)])
    return child

#picks x random subjects from a population and stores individual fitness and index
def xRandom (population, x):
    chosen = []
    ind = []
    for i in range(0, x):
        y = randint(0, len(population))
        if y not in ind:
            ind = ind + [y]
            chosen = chosen + population[y]
    return chosen,ind

def best2 (selection, indexes):
    best = []
    if individualFitness(selection[0]) <= individualFitness(selection[1]):
        x = 0
        y = 1
    else:
        x = 1
        y = 0
    for i in range(2, len(selection)):
        if individualFitness(selection[i]) <= individualFitness(selection[x]):
            y = x
            x = i
        elif individualFitness(selection[i]) <= individualFitness(selection[y]):
            y = i
    best = [indexes[x], indexes[y]]
    return best

def replace (population, ind, subject):
    population[ind] = subject