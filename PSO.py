import time
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import copy
import random
from RandomNumberGenerator import *
from scipy.stats import uniform

# Wartość współczynnika bezwładności (w) wpływa na zdolność cząstek do zachowania poprzedniej prędkości.
# #Wraz ze wzrostem wartości tego parametru, zwiększa się zdolność cząstek do przeszukiwania nowych rejonów przestrzeni rozwiązań.
# Wzór -> w=1-aktualnaIteracja/maxLiczbaIteracji

# c - tempo uczenia (od 0 do 1) (nazywane współczynnikiem ścisku)
# Wzór -> omega = cl+cg (musi być większe niż 4)        c = 2/|2-omega-sqrt(omega*omega-4*omega)|

class PSO():

    _population = 10
    _size = 2
    _iterations = 100
    _w = 1
    _c = 1
    _cl = 2.1
    _cg = 2.1
    _L = -100
    _U = 100
    
    _populationList = []
    _speedList = []
    _localBestList = []

    _globalBest = 0

    def __init__(self, size, population, iterations, cl, cg):
        self._size = size
        self._population = population
        self._iterations = iterations
        self._cl = cl
        self._cg = cg
        self._populationList = [
            [0 for i in range(size)] for j in range(population)]
        self._speedList = [
            [0 for i in range(size)] for j in range(population)]
        self._localBestList = [0 for i in range(population)]

    def simplescore(self, permutation):
        score = 0
        for i in range(self._size):
            score=score+(permutation[i]**2)
        return score

    def solve(self):

        








        #print(round(uniform.rvs(),5))
        #uniform.rvs(loc=0,scale=1)


#ZMIENNE

n = 20                  #rozmiar problemu
k = 100                 #liczba czastek
iterations = 1000        #liczba iteracji

#PARAMETRY

#Współczynnik dążenia do najlepszego lokalnego rozwiązania (ol)
#Im większa wartość tego parametru tym większa skłonność cząstki do oscylacji wokół swojej najlepszej pozycji.
cl = 2

#Współczynnik dążenia do najlepszego globalnego rozwiązania (og) 
#Zwiększanie wartości tego parametru powoduje zwiększenie tendencji do grupowania się cząstek wokół najlepszego globalnego rozwiązania.
cg = 4

#To problem unimodalny, więc zalecane aby "og" lepszy niż "ol"

# φ1>0 oraz φ2=0 Każda cząstka realizuje stochastyczny algorytm wspinania się na wzgórze(ang. hill climbing).
# φ1=0 oraz φ2>0 Cały rój realizuje stochastyczny algorytm wspinania się na wzgórze.
# φ1=φ2>0 Cząstka przyciągana jest przez średnią z pi oraz g.
# φ1>φ2 Zalecane w przypadku problemów multimodalnych.
# φ1<φ2 Zalecane w przypadku problemów unimodalnych.
# niskie φ1, φ2 Gładkie trajektorie cząstek.
# wysokie φ1, φ2 Gwałtowne trajektorie cząstek.


def main():
    
    print("Rozwiązanie problemu optymalizacji funkcji ciągłej Sphere function przy pomocy PSO")

    x = PSO(n, k, iterations, cl, cg)
    wynik = x.solve()


main()
