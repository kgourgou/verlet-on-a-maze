import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

from simulator.particle import Particle, create_particle, particle_distance
from simulator.plotting_utils import draw_lines, draw_points
from simulator.conditions import apply_boundary_condition, apply_link_constraints

particles = [
    Particle(curr_pos=np.array([1.0, 10.0]), prev_pos=np.array([1, 10.0])),
    Particle(curr_pos=np.array([0, 13.0]), prev_pos=np.array([0, 16.0])),
    create_particle([-0.5, 11.0]),
    create_particle([0.3, 0.4], [0.9, 0.4]),
]

links = {0: [1], 1: [2], 2: [3]}


initial_link_distances = {}
for from_ in links:
    initial_link_distances[from_] = {
        m: particle_distance(particles[from_], particles[m]) for m in links[from_]
    }


fig = plt.figure()
camera = Camera(fig)


NUMBER_OF_TIMESTEPS = 100
for _ in range(NUMBER_OF_TIMESTEPS):

    # draw points
    draw_points(particles)

    # draw lines
    draw_lines(particles, links)
    camera.snap()

    # particle loop
    for i, p in enumerate(particles):

        p.update_location()

        # check boundary constraint
        apply_boundary_condition(p)

        # link constraints
    apply_link_constraints(
        particles,
        links,
        initial_link_distances,
        pinned_particles={0: [1.0, 10.0], 2: [-0.5, 11.0]},
        number_of_passes=10,
    )


# plt.show()
animation = camera.animate()
plt.show()
