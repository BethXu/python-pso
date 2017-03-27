import random

from fitness import Fitness

class Particle(object):
    def __init__(self, position):
        self._position = position
        self._dimensions = len(position)
        self._best_position = position
        self._best_fitness = Fitness.calculate(position)
        self._velocity = [self.get_random_velocity() for _ in range(self._dimensions)]

    def get_random_velocity(self):
        u = abs(Fitness.UPPER_BOUND - Fitness.LOWER_BOUND)
        return random.uniform(-u, u)

    @property
    def position(self):
        return self._position

    def _update_best_position(self):
        new_fitness = Fitness.calculate(self._position)
        if new_fitness < self._best_fitness:
            self._best_fitness = new_fitness
            self._best_position = self._position

    @property
    def best_position(self):
        return self._best_position

    @property
    def velocity(self):
        return self._velocity

    def update(self, inertia, nostalgia, envy, global_best):
        # print self._velocity
        for i in range(self._dimensions):
            # print i
            random_self = random.random()
            # print random_self
            random_global = random.random()
            # print random_global
            # Inertia
            self._velocity[i] = self._velocity[i] * inertia
            # Update own velocity according to memory of previous personal best position
            self._velocity[i] += nostalgia * random_self * (self._best_position[i] - self._position[i])
            # Update own velocity according to memory of global best position
            self._velocity[i] += envy * random_global * (global_best[i] - self._position[i])
            self._position[i] += self._velocity[i]
        self._update_best_position()
        # print v

