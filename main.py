import copy

from InstanceGenerator import instanceGenerator
from Route import Route
import random
import operator
from cross import Cross
from neighburhood import swaping, backwards
from random import choices

def main():
    MAX_CHANGE_LIMIT = 10
    ITERATIONS = 50000
    PROBLEM_SIZE = 5
    SEED = 20
    PROBLEM_MATRIX = instanceGenerator(SEED, PROBLEM_SIZE)
    BEES_AMOUNT = 5
    CROSS_POINTS = 2

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
                    print("NEW BEST")
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
                        print("NEW BEST")
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
                        print("NEW BEST")
                else:
                    BEES_LIST[i].increment_count()
                    if BEES_LIST[i].get_count() > MAX_CHANGE_LIMIT:  ##ABOVE MAX CHANGE COUNT (Nowy osobnik do poplacji)
                        random.shuffle(init_list)
                        x = Route(copy.deepcopy(init_list), PROBLEM_MATRIX)
                        BEES_LIST[i] = copy.deepcopy(x)

        #POSORTUJ PO OBSERWATORACH
        BEES_LIST.sort(key=operator.attrgetter('_value'))

    print("BEST WAY THAT HAS BEEN FINDED: ", BEST_SOLUTION.get_value())
    print("BEST route THAT HAS BEEN FINDED: ", BEST_SOLUTION.get_route_list())

main()
