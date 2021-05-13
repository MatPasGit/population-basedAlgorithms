import random

from Route import Route


class Cross:
    _parent_one = []
    _parent_sec = []
    _cross_points = 2
    PROBLEM_MATRIX = []

    def __init__(self, parent1, parent2, cross_points, problem_matrix):
        self._parent_one = parent1
        self._parent_sec = parent2
        self._cross_points = cross_points
        self.PROBLEM_MATRIX = problem_matrix

    def OX_cross(self):
        allels = self._cross_points + 1
        allels = int( len(self._parent_one)/allels) +1


        child=[]

        luck = random.randint(0, 1)            #losowanie chromosomu
        if luck == 0:
            for i in range(0, allels):
                child.append(self._parent_one[i])
        if luck == 1:
            for i in range(allels, allels+allels):
                child.append(self._parent_one[i])

        for i in range(0, len(self._parent_sec)):
            if self._parent_sec[i] in child :
                continue
            else:
                child.append(self._parent_sec[i])

        return Route(child, self.PROBLEM_MATRIX)

