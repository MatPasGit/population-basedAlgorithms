import time
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import copy
import random
from RandomNumberGenerator import *

class PSO():

    _population = 100

    def __init__(self, population):
        self._population = population

    def solve(self):
        print("TU JA")


#ZMIENNE

n = 20          #rozmiar problemu
p = 100          #liczba osobników w stadzie

def main():
    
    print("Rozwiązanie problemu optymalizacji funkcji ciągłej Sphere function przy pomocy PSO")

    x = PSO(p)
    x.solve()


main()