from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

GRAVITY = 0.9
DRAG = 0.3


@dataclass
class Particle:
    # holds the current and previous position of a particle
    curr_pos: np.array
    prev_pos: np.array

    def update_location(self):
        dx = self.compute_dx()
        self.prev_pos = self.curr_pos
        self.curr_pos += dx
        self.curr_pos -= np.array([0, GRAVITY])

    def compute_speed(self):
        dx = self.compute_dx()
        print(self.curr_pos)
        print(self.prev_pos)
        speed = np.sqrt(np.sum(dx ** 2))
        return speed

    def compute_dx(self):
        return (self.curr_pos - self.prev_pos) * DRAG

    def __repr__(self):
        return f"{self.curr_pos}"

    def show(self):
        plt.plot(self.curr_pos[0], self.curr_pos[1], "ro")
