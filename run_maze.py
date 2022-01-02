import numpy as np
from pymaze.maze_manager import MazeManager
from pymaze.maze import Maze
from itertools import product
from collections import defaultdict
from simulator.particle import create_particle
from simulator.simulator import simulate

import matplotlib.pyplot as plt
from celluloid import Camera

manager = MazeManager()

# We can add mazes to the manager two different ways.
# The first way, we specify the maze dimensions. The maze that is created gets returned back to you.

WIDTH = 10
HEIGHT = 10

maze = manager.add_maze(WIDTH, HEIGHT)

# construct initial grid
particles = defaultdict(lambda x=None: None)
links = defaultdict(list)

mapping = {
    "top": np.array([0, 1]),
    "bottom": np.array([0, -1]),
    "left": np.array([-1, 0]),
    "right": np.array([1, 0]),
}


for i, j in product(range(WIDTH), range(HEIGHT)):
    particles[(i, j)] = create_particle([i, j])
    for wall, exists in maze.grid[i][j].walls.items():
        if exists:
            new_link = tuple(mapping[wall] + np.array([i, j]))
            if min(new_link) < 0 or max(new_link) > (WIDTH - 1):
                continue

            links[(i, j)].append(new_link)

fig = plt.figure()
camera = Camera(fig)

# TODO make them snap at integer coordinates.


def default_distance():
    return defaultdict(lambda x=None: 1.0)


initial_link_distances = defaultdict(default_distance)
pinned_particles = {(0, 0): np.array([0.0, 9.0]), (9, 9): np.array([100.0, 9.0])}


simulate(
    particles,
    links,
    pinned_particles,
    initial_link_distances,
    camera,
    number_of_steps=40,
    number_of_passes=40,
)
animation = camera.animate()
plt.show()
