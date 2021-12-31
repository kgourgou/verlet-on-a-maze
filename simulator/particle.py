import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

GRAVITY = 0.9
DRAG = 1


def create_particle(curr_pos, prev_pos=None):
    if prev_pos:
        return Particle(curr_pos=np.array(curr_pos), prev_pos=np.array(prev_pos))
    else:
        return Particle(curr_pos=np.array(curr_pos), prev_pos=np.array(curr_pos))


def particle_distance(p1, p2):
    return norm(p1.curr_pos - p2.curr_pos)


class Particle:
    # holds the current and previous position of a particle
    def __init__(self, curr_pos: np.array, prev_pos: np.array):
        self.init_pos = curr_pos
        self.curr_pos = curr_pos.astype(np.float)
        self.prev_pos = prev_pos.astype(np.float)

    def update_location(self):
        dx = self.compute_dx()
        self.prev_pos = self.curr_pos
        self.curr_pos += dx
        self.curr_pos -= np.array([0, GRAVITY])

    def compute_speed(self):
        dx = self.compute_dx()
        speed = norm(dx)
        return speed

    def compute_dx(self):
        return (self.curr_pos - self.prev_pos) * DRAG

    def __repr__(self):
        return f"{self.curr_pos}"

    def show(self):
        plt.plot(self.curr_pos[0], self.curr_pos[1], "ro")
