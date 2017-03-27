import random
import copy

from fitness import Fitness
from particle import Particle

class PSO(object):

    DIMENSIONS = 2
    INERTIA = 0.9
    NOSTALGIA = 0.5
    ENVY = 0.5

    def __init__(self, n):
        self.swarm_size = n
        self.swarm = [self.random_particle() for _ in range(self.swarm_size)]
        self.best_position = self.swarm[0].position
        self.set_best()
        while self._best_fitness != 0:
            self.update()

    def random_particle(self):
        return Particle([self.random_position(), self.random_position()])

    def random_position(self):
        return random.uniform(Fitness.LOWER_BOUND, Fitness.UPPER_BOUND)

    def set_best(self):
        self._best_fitness = Fitness.calculate(self.best_position)
        for particle in self.swarm:
            this_fitness = Fitness.calculate(particle.position)
            if this_fitness < self._best_fitness:
                self._best_fitness = this_fitness
                self.best_position = copy.deepcopy(particle.position)


    def update(self):
        self.set_best()
        print self._best_fitness
        for particle in self.swarm:
            particle.update(PSO.INERTIA, PSO.NOSTALGIA, PSO.ENVY, self.best_position)

if __name__ == '__main__':
    PSO(1000)

