import math

class Fitness(object):

    LOWER_BOUND = -5.12
    UPPER_BOUND = 5.12

    # Rastrigin function
    @staticmethod
    def calculate(position):
        fitness = 10*len(position)
        for i in range(len(position)):
            fitness += position[i]**2 - (10*math.cos(2*math.pi*position[i]))
        return fitness
