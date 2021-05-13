import copy

from InstanceGenerator import instanceGenerator
from Route import Route
import random
import operator
from cross import Cross
from neighburhood import swaping, backwards
from random import choices

import time
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.stats import uniform

def main(iterations, problem_size, bees_amount):
    MAX_CHANGE_LIMIT = 20
    CROSS_POINTS = 2
    SEED = 20

    ITERATIONS = iterations
    PROBLEM_SIZE = problem_size
    BEES_AMOUNT = bees_amount
    
    PROBLEM_MATRIX = instanceGenerator(SEED, PROBLEM_SIZE)
    
    #INIT SOLUTION
    init_list = []
    for i in range(0, PROBLEM_SIZE):
        init_list.append(i)

    BEES_LIST=[]
    BEST_SOLUTION = Route(init_list, PROBLEM_MATRIX)

    # INITIALIZING BEES
    for i in range(0, BEES_AMOUNT):
        random.shuffle(init_list)
        x = Route( copy.deepcopy(init_list), PROBLEM_MATRIX)
        if i == 0:
            BEST_SOLUTION = copy.deepcopy(x)
        if x.get_value() > BEST_SOLUTION.get_value():
            BEST_SOLUTION =  copy.deepcopy(x)
        BEES_LIST.append(x)


    BEES_LIST.sort(key=operator.attrgetter('_value'))

    loop = 0
    while loop < ITERATIONS:
        loop += 1

    #ZBIERACZE
        for i in range(0, len(BEES_LIST)):
            child = None

            luck = random.randint(0, 1)
            if luck == 0:
                if i ==  len(BEES_LIST) - 1:
                    child = Cross(BEES_LIST[i].get_route_list(), BEES_LIST[0].get_route_list(), CROSS_POINTS, PROBLEM_MATRIX)
                else:
                    child = Cross(BEES_LIST[i].get_route_list(), BEES_LIST[i+1].get_route_list(), CROSS_POINTS,PROBLEM_MATRIX )
            if luck == 1:
                if i ==  0:
                    child = Cross(BEES_LIST[i].get_route_list(), BEES_LIST[len(BEES_LIST) - 1].get_route_list(), CROSS_POINTS, PROBLEM_MATRIX)
                else:
                    child = Cross(BEES_LIST[i].get_route_list(), BEES_LIST[i-1].get_route_list(), CROSS_POINTS,PROBLEM_MATRIX )
            new_solution = child.OX_cross()

            if(new_solution.get_value() > BEES_LIST[i].get_value() ):
                BEES_LIST[i] = copy.deepcopy(new_solution)
                if new_solution.get_value() > BEST_SOLUTION.get_value():
                    BEST_SOLUTION = copy.deepcopy(new_solution)
                    #print("NEW BEST")
            else:
                BEES_LIST[i].increment_count()
                if BEES_LIST[i].get_count() > MAX_CHANGE_LIMIT:     ##ABOVE MAX CHANGE COUNT (Nowy osobnik do populacji)
                    random.shuffle(init_list)
                    x = Route(copy.deepcopy(init_list), PROBLEM_MATRIX)
                    BEES_LIST[i] = copy.deepcopy(x)

        #POSORTUJ PO ZBIERACZACH
        BEES_LIST.sort(key=operator.attrgetter('_value'))

        #LISTA KOLA RULETKI
        roulette = []                               #dystrybuanta dla indeksów które będą losowane
        probablility = 0
        for i in range(len(BEES_LIST)):
            new_score = BEES_LIST[len(BEES_LIST)-1].get_value()-BEES_LIST[i].get_value()
            probablility += new_score

        for i in range(len(BEES_LIST)):
            b = BEES_LIST[len(BEES_LIST)-1].get_value() - BEES_LIST[i].get_value()
            roulette.append(( b /probablility) )    #NAPRAWIC KOLO RULETKI

        #print("ROULETTE: ", roulette)
        #c = 0
        #for i in range(0, len(roulette)):
        #    c+= roulette[i]
        #print(c)

        #OBSERWATORZY
        index = []
        for i in range(0, len(BEES_LIST)):
            index.append(i)

        for i in range(0, len(BEES_LIST)):
            bee_change = choices(index, roulette)
            bee_changer = bee_change[0] #choices zwraca liste i trzeba zrzucic do inta bo inaczej sie nie wywola reszta

            luck = random.randint(0, 1)
            if luck == 0:
                x = BEES_LIST[bee_changer]
                xa = swaping(x.get_route_list())
                x = Route(xa, PROBLEM_MATRIX)
                if (x.get_value() > BEES_LIST[bee_changer].get_value()):
                    BEES_LIST[i] = copy.deepcopy(x)
                    if x.get_value() > BEST_SOLUTION.get_value():
                        BEST_SOLUTION = copy.deepcopy(x)
                        #print("NEW BEST")
                else:
                    BEES_LIST[i].increment_count()
                    if BEES_LIST[i].get_count() > MAX_CHANGE_LIMIT:  ##ABOVE MAX CHANGE COUNT (Nowy osobnik do poplacji)
                        random.shuffle(init_list)
                        x = Route(copy.deepcopy(init_list), PROBLEM_MATRIX)
                        BEES_LIST[i] = copy.deepcopy(x)
            else:
                x = BEES_LIST[bee_changer]
                xa = backwards(x.get_route_list())
                x = Route(xa, PROBLEM_MATRIX)
                if (x.get_value() > BEES_LIST[bee_changer].get_value()): ##Jesli lepsza od istniejacej
                    BEES_LIST[i] = copy.deepcopy(x)
                    if x.get_value() > BEST_SOLUTION.get_value():
                        BEST_SOLUTION = copy.deepcopy(x)
                        #print("NEW BEST")
                else:
                    BEES_LIST[i].increment_count()
                    if BEES_LIST[i].get_count() > MAX_CHANGE_LIMIT:  ##ABOVE MAX CHANGE COUNT (Nowy osobnik do poplacji)
                        random.shuffle(init_list)
                        x = Route(copy.deepcopy(init_list), PROBLEM_MATRIX)
                        BEES_LIST[i] = copy.deepcopy(x)

        #POSORTUJ PO OBSERWATORACH
        BEES_LIST.sort(key=operator.attrgetter('_value'))

    print("BEST WAY THAT HAS BEEN FINDED: ", BEST_SOLUTION.get_value())
    print("BEST ROUTE THAT HAS BEEN FINDED: ", BEST_SOLUTION.get_route_list())
    return BEST_SOLUTION.get_value()


wyniki = []
wynikiczasowe = []

tempIterations = 1500
tempProblemSize = 5
tempBeesAmount = 100

for tempProblemSize in range(5, 26):
    for tempBeesAmount in [30, 70, 100]:
        for tempIterations in [500, 1000, 1500]:
        
            start = time.time()
            wynik = main(tempIterations, tempProblemSize, tempBeesAmount)
            end = time.time()
            czas = end - start

            print("===Wynik dla n="+str(tempProblemSize)+", bees="+str(tempBeesAmount)+", iter="+str(tempIterations))
            wyniki.append(wynik)
            wynikiczasowe.append(czas)

argumenty = np.linspace(1, 21, 21)

plt.plot(argumenty, wyniki[::9], label="bees=30 - iter=500")
plt.plot(argumenty, wyniki[1::9], label="bees=30 - iter=1000")
plt.plot(argumenty, wyniki[2::9], label="bees=30 - iter=1500")
plt.plot(argumenty, wyniki[3::9], label="bees=70 - iter=500")
plt.plot(argumenty, wyniki[4::9], label="bees=70 - iter=1000")
plt.plot(argumenty, wyniki[5::9], label="bees=70 - iter=1500")
plt.plot(argumenty, wyniki[6::9], label="bees=100 - iter=500")
plt.plot(argumenty, wyniki[7::9], label="bees=100 - iter=1000")
plt.plot(argumenty, wyniki[8::9], label="bees=100 - iter=1500")

plt.grid(True)
plt.xlabel("Liczba argumentow (n)")
plt.ylabel("Wynik trasy")
plt.title("Wykres wyników w zależności od parametorów")
plt.legend()
plt.savefig("WykresABCWyniki.jpg", dpi=72)
plt.show()

plt.plot(argumenty, wynikiczasowe[::9], label="bees=30 - iter=500")
plt.plot(argumenty, wynikiczasowe[1::9], label="bees=30 - iter=1000")
plt.plot(argumenty, wynikiczasowe[2::9], label="bees=30 - iter=1500")
plt.plot(argumenty, wynikiczasowe[3::9], label="bees=70 - iter=500")
plt.plot(argumenty, wynikiczasowe[4::9], label="bees=70 - iter=1000")
plt.plot(argumenty, wynikiczasowe[5::9], label="bees=70 - iter=1500")
plt.plot(argumenty, wynikiczasowe[6::9], label="bees=100 - iter=500")
plt.plot(argumenty, wynikiczasowe[7::9], label="bees=100 - iter=1000")
plt.plot(argumenty, wynikiczasowe[8::9], label="bees=100 - iter=1500")

plt.grid(True)
plt.xlabel("Liczba argumentow (n)")
plt.ylabel("Czas [s]")
plt.title("Wykres czasu działania w zależności od parametrów")
plt.legend()
plt.savefig("WykresABCWynikiCzasowe.jpg", dpi=72)
plt.show()
