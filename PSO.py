import time
import copy
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import math
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
    _globalBest = []

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

        self._localBestList = [
            [0 for i in range(size)] for j in range(population)]
        self._globalBest = [0 for i in range(size)]

    def simplescore(self, permutation):
        score = 0
        for i in range(self._size):
            score=score+(permutation[i]**2)
        return score

    def solve(self):

        for i in range(self._size):
            self._populationList[0][i] = round(uniform.rvs(loc=self._L, scale=self._U-self._L), 5)

        self._localBestList[0] = copy.deepcopy(self._populationList[0])
        self._globalBest = copy.deepcopy(self._populationList[0])

        for i in range(self._size):
            self._speedList[0][i] = round(uniform.rvs(loc=self._L-self._U, scale=2*self._U-2*self._L), 5)

        for j in range(self._population):
            if j == 0:
                continue
            
            for i in range(self._size):
                self._populationList[j][i] = round(uniform.rvs(loc=self._L, scale=self._U-self._L), 5)
            
            self._localBestList[j] = copy.deepcopy(self._populationList[j])

            if self.simplescore(self._populationList[j]) < self.simplescore(self._globalBest):
                self._globalBest = copy.deepcopy(self._populationList[j])
                #print("Najlepsza: "+str(self._globalBest))

            for i in range(self._size):
                self._speedList[j][i] = round(uniform.rvs(loc=self._L-self._U, scale=2*self._U-2*self._L), 5)

        omega = self._cl+self._cg
        self._c = 2/math.fabs(2-omega-math.sqrt(omega**2-4*omega))

        for actualIter in range(self._iterations):

            self._w = 1-(actualIter+1)/self._iterations

            for j in range(self._population):

                for i in range(self._size):

                    rl = round(uniform.rvs(),5)
                    rg = round(uniform.rvs(),5)
                    a = self._w*self._speedList[j][i]
                    b = self._cl*rl * (self._localBestList[j][i]-self._populationList[j][i])
                    c = self._cg*rg * (self._globalBest[i]-self._populationList[j][i])
                    self._speedList[j][i] = a+b+c

                    self._populationList[j][i] = self._populationList[j][i] + self._c*self._speedList[j][i]

                if self.simplescore(self._populationList[j]) < self.simplescore(self._localBestList[j]):
                    self._localBestList[j] = copy.deepcopy(self._populationList[j])

                if self.simplescore(self._populationList[j]) < self.simplescore(self._globalBest):
                    self._globalBest = copy.deepcopy(self._populationList[j])
                    #print("Najlepsza: "+str(self._globalBest))

        return self._globalBest


#ZMIENNE

n = 3                  #rozmiar problemu
k = 30                 #liczba czastek
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
    
    wyniki = []
    wynikiczasowe = []


    print("Rozwiązanie problemu optymalizacji funkcji ciągłej Sphere function przy pomocy PSO")

    for n in range(1,16):
        for k in [10,20]:
            for iterations in [100,200]:
                for cl in [2,3,4]:
                    cg = 6-cl

                    start = time.time()
                    x = PSO(n, k, iterations, cl, cg)
                    wynik = x.solve()
                    end = time.time()
                    czas = end - start

                    print("===Wynik dla n="+str(n)+", k="+str(k)+", iter="+str(iterations)+", cl="+str(cl)+", cg="+str(cg))
                    print("Koniec: "+str(wynik))
                    print("Wartosc funkcji: "+str(x.simplescore(wynik)))
                    print("Czas: "+str(czas))

                    wyniki.append(x.simplescore(wynik))
                    wynikiczasowe.append(czas)


    argumenty = np.linspace(1, 15, 15)

    plt.plot(argumenty, wyniki[::12], label="k=10 - iter=100 - 2i4")
    plt.plot(argumenty, wyniki[1::12], label="k=10 - iter=100 - 3i3")
    plt.plot(argumenty, wyniki[2::12], label="k=10 - iter=100 - 4i2")
    plt.plot(argumenty, wyniki[3::12], label="k=10 - iter=200 - 2i4")
    plt.plot(argumenty, wyniki[4::12], label="k=10 - iter=200 - 3i3")
    plt.plot(argumenty, wyniki[5::12], label="k=10 - iter=200 - 4i2")
    plt.plot(argumenty, wyniki[6::12], label="k=20 - iter=100 - 2i4")
    plt.plot(argumenty, wyniki[7::12], label="k=20 - iter=100 - 3i3")
    plt.plot(argumenty, wyniki[8::12], label="k=20 - iter=100 - 4i2")
    plt.plot(argumenty, wyniki[9::12], label="k=20 - iter=200 - 2i4")
    plt.plot(argumenty, wyniki[10::12], label="k=20 - iter=200 - 3i3")
    plt.plot(argumenty, wyniki[11::12], label="k=20 - iter=200 - 4i2")

    plt.grid(True)
    plt.xlabel("Liczba argumentow (n)")
    plt.ylabel("Wynik dzialania funkcji")
    plt.title(
        "Wykres wyników w zależności od parametorów")
    plt.legend()
    plt.savefig("WykresPSOWyniki.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiczasowe[::12], label="k=10 - iter=100 - 2i4")
    plt.plot(argumenty, wynikiczasowe[1::12], label="k=10 - iter=100 - 3i3")
    plt.plot(argumenty, wynikiczasowe[2::12], label="k=10 - iter=100 - 4i2")
    plt.plot(argumenty, wynikiczasowe[3::12], label="k=10 - iter=200 - 2i4")
    plt.plot(argumenty, wynikiczasowe[4::12], label="k=10 - iter=200 - 3i3")
    plt.plot(argumenty, wynikiczasowe[5::12], label="k=10 - iter=200 - 4i2")
    plt.plot(argumenty, wynikiczasowe[6::12], label="k=20 - iter=100 - 2i4")
    plt.plot(argumenty, wynikiczasowe[7::12], label="k=20 - iter=100 - 3i3")
    plt.plot(argumenty, wynikiczasowe[8::12], label="k=20 - iter=100 - 4i2")
    plt.plot(argumenty, wynikiczasowe[9::12], label="k=20 - iter=200 - 2i4")
    plt.plot(argumenty, wynikiczasowe[10::12], label="k=20 - iter=200 - 3i3")
    plt.plot(argumenty, wynikiczasowe[11::12], label="k=20 - iter=200 - 4i2")

    plt.grid(True)
    plt.xlabel("Liczba argumentow (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres czasu działania w zależności od parametrów")
    plt.legend()
    plt.savefig("WykresPSOWynikiCzasowe.jpg", dpi=72)
    plt.show()

main()
