from random import randint

#base subject to create population without repetitions
baseSubject = "000001010011100101110111"

#solution for test purposes
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
        population[i] = shuffle(200, baseIndividual)
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
    fitness = fitness / (len(population))
    return fitness

#also returns best subject fitness
def APFwithBestSubject (population):
    fitness = 0
    best = 28
    for i in range(0, len(population)):
        x = individualFitness(population[i])
        if x < best:
            best = x
        fitness = fitness + x
    fitness = fitness / (len(population))
    return fitness,best

def edgeRecombination (parent1, parent2):
    edges = []
    for i in range(0, 7):
        part = []
        for e in range(0, 7):
            ind = e*3
            aux = parent1[ind:(ind+3)]
            value = int(bin(int(aux, 2)),2)
            if value == i:
                if e == 0:
                    part = part + [int(bin(int(parent1[((e + 1) * 3):(((e + 1) * 3) + 3)], 2)), 2)]
                    break
                elif e == 1:
                    part = part + [int(bin(int(parent1[((e - 1) * 3):(((e - 1) * 3) + 3)], 2)), 2)]
                    break
                else:
                    part = part + [int(bin(int(parent1[((e+1)*3):(((e+1)*3) + 3)], 2)), 2)] + [int(bin(int(parent1[((e-1)*3):(((e-1)*3) + 3)], 2)), 2)]
                    break
            for f in range(0, 7):
                ind2 = f * 3
                aux2 = parent2[ind2:(ind2 + 3)]
                value = int(bin(int(aux2, 2)), 2)
                if value == i:
                    if e == 0:
                        part = part + [int(bin(int(parent2[((e + 1) * 3):(((e + 1) * 3) + 3)], 2)), 2)]
                        break
                    elif e == 1:
                        part = part + [int(bin(int(parent2[((e - 1) * 3):(((e - 1) * 3) + 3)], 2)), 2)]
                        break
                    else:
                        part = part + [int(bin(int(parent2[((e + 1) * 3):(((e + 1) * 3) + 3)], 2)), 2)] + [int(bin(int(parent2[((e - 1) * 3):(((e - 1) * 3) + 3)], 2)), 2)]
                        break
        edges = edges + [part]
    


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

#xRandom and best2 must be used together
#picks x random subjects from a population and stores individual fitness and index
def xRandom (population, x):
    chosen = []
    ind = []
    for i in range(0, x):
        y = randint(0, (len(population) - 1))
        if y not in ind:
            ind = ind + [y]
            chosen = chosen + [population[y]]
    return chosen,ind

#choses the best 2 individuals out of the xRandom result
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

def findXWorst (population, x):
    worst = list(range(0,x))
    for i in range(x, len(population)):
        for e in range(0, x):
            if individualFitness(population[i]) > individualFitness(population[(worst[e])]):
                worst[e] = i
                break
    return worst

def findXBest (population, x):
    best = list(range(0,x))
    for i in range(x, len(population)):
        for e in range(0, x):
            if individualFitness(population[i]) < individualFitness(population[(best[e])]):
                best[e] = i
                break
    return best

def getSolution (population):
    solution = ""
    for i in range(0, len(population)):
        if individualFitness(population[i]) == 0:
            solution = population[i]
    return solution

#test 1: cut and crossfill
#parents = best 2 out of 5
#survivors = replace worst
#population size = 100
#stop condition = solution or x iterations
def test1(iterations):
    population = initialPopulation(100, baseSubject)

    for i in range(0, iterations):
        avgFitness, bestFitness = APFwithBestSubject(population)

        #print ("Iteration: " + str(i) + ", Average Fitness: " + str(avgFitness) + ", BestFitness: " + str(bestFitness) + ".")

        if avgFitness == 0 or i == (iterations - 1):
            print ("Iteration: " + str(i) + ", Average Fitness: " + str(avgFitness) + ", BestFitness: " + str(bestFitness) + ".")
            break

        tournament, indexes = xRandom(population, 5)
        parents = best2(tournament, indexes)
        cut = randint(2, 5)
        child1 = cutAndCrossfill(population[parents[0]], population[parents[1]], cut)
        child2 = cutAndCrossfill(population[parents[1]], population[parents[0]], cut)
        mutation = shuffle(1, population[randint(0, (len(population) -  1))])

        worst = findXWorst(population, 3)

        replace(population, worst[0], child1)
        replace(population, worst[1], child2)
        replace(population, worst[2], mutation)

#test 2: also cut and crossfill, but picks the 2 best parents out of the whole population (elitist)
#merged with test3 (run with recombinations and mutations = 1)

#test 3: same as test 2 but with variable number of recombinations and mutations
#note: recombinations represent the total number of parents pairs that are going to be used in the test
def test2(iterations, recombinations, mutations):
    population = initialPopulation(100, baseSubject)

    for i in range(0, iterations):
        avgFitness, bestFitness = APFwithBestSubject(population)

        #print ("Iteration: " + str(i) + ", Average Fitness: " + str(avgFitness) + ", BestFitness: " + str(bestFitness) + ".")

        if avgFitness == 0 or i == (iterations - 1):
            print ("Iteration: " + str(i) + ", Average Fitness: " + str(avgFitness) + ", BestFitness: " + str(bestFitness) + ".")
            break

        parents = findXBest(population, (recombinations * 2))
        childs = []
        for e in range(0, len(parents), 2):
            cut = randint(2, 5)
            childs = childs + [cutAndCrossfill(population[parents[0]], population[parents[1]], cut)]
            childs = childs + [cutAndCrossfill(population[parents[1]], population[parents[0]], cut)]

        mutate = []
        for f in range(0, mutations):
            mutate = mutate + [shuffle(1, population[randint(0, (len(population) - 1))])]

        worst = findXWorst(population, (len(mutate) + len(childs)))
        for g in range(0, len(worst)):
            if g <= (len(mutate) - 1):
                replace(population, worst[g], mutate[g])
            else:
                replace(population, worst[g], childs[(g - len(mutate))])

for i in range(0, 10):
    test2(1000, 15, 20)