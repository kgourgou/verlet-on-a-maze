import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

from simulator.particle import Particle, create_particle, particle_distance
from simulator.simulator import simulate

particles = [
    Particle(curr_pos=np.array([1.0, 10.0]), prev_pos=np.array([1, 13.0])),
    Particle(curr_pos=np.array([0, 13.0]), prev_pos=np.array([0, 16.0])),
    create_particle([-0.5, 11.0]),
    create_particle([0.3, 9.0], [1.0, 9.0]),
]

links = {0: [1], 1: [2], 2: [3]}

PINNED_PARTICLES = {0: [1.0, 10.0], 3: [-100.0, 10.0]}

initial_link_distances = {}
for from_ in links:
    initial_link_distances[from_] = {
        m: particle_distance(particles[from_], particles[m]) for m in links[from_]
    }


fig = plt.figure()
camera = Camera(fig)


simulate(particles, links, PINNED_PARTICLES, initial_link_distances, camera)


# plt.show()
animation = camera.animate()
plt.show()
