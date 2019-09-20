from random import randint

#base subject to create population without repetitions
baseSubject = "000001010011100101110111"

#solution for test purpose
solution = "100000111011001110010101"

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

def individualFitness (baseIndividual):
    colisions = 0
    for i in range(0, 7):
        ind = i*3
        aux = baseIndividual[ind:(ind+3)]
        value1 = int(bin(int(aux, 2)),2)
        for e in range((i+1), 8):
            ind2 = e * 3
            aux2 = baseIndividual[ind2:(ind2 + 3)]
            value2 = int(bin(int(aux2, 2)), 2)
            distance = e - i
            if ((value1 + distance) == value2) or ((value1 - distance) == value2):
                colisions = colisions + 1
    return(colisions)

x = individualFitness(baseSubject)
print x
