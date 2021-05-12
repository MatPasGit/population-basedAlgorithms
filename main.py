from InstanceGenerator import instanceGenerator
from Route import Route


def main():
    problem_instance = instanceGenerator(20, 5)
    r = Route([0,1,2,3,4], problem_instance)
    print(r.get_value())
    print(r.get_route_list())


main()
