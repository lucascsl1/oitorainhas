from random import randint

baseSubject = "000001010011100101110111"

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

#def individualFitness (baseIndividual):
#    colisions = 0
#    for i in range(0, 6):
#        value1 = ''.join(format(ord(n), 'b') for n in baseIndividual[(i*3):i+3])

aux =
v = ''.join(format(ord(n), 'b') for n in baseSubject[0:3])
print(v)