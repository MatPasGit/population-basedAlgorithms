

class Route:

    _route_list = []
    _value = 0

    def __init__(self,route_list, problem_instance ):
        self._route_list = route_list
        self._value = self.objective_function(problem_instance)

    def objective_function(self,  problem_instance):
         value = 0

         for i in range(0, len(self._route_list) - 1 ):
             value += problem_instance[self._route_list[i] ][ self._route_list[i+1] ]

         value += problem_instance[self._route_list[len(self._route_list)-1]][self._route_list[0]]

         return value

    def get_route_list(self):
        return self._route_list

    def get_value(self):
        return self._value

    def set_route_list(self, route_list, problem_instance):
        self._route_list = route_list
        self._value = self.objective_function(problem_instance)



