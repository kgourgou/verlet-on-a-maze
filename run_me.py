import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

from simulator.particle import Particle


def create_particle(curr_pos):
    return Particle(curr_pos=np.array(curr_pos), prev_pos=np.array(curr_pos))


particles = [
    Particle(curr_pos=np.array([1.0, 10.0]), prev_pos=np.array([1, 10.0])),
    Particle(curr_pos=np.array([0, 10.0]), prev_pos=np.array([0, 10.0])),
    create_particle([0.0, 11.0]),
]

links = {0: [1, 2], 1: [2]}


def dist_particles(p1, p2):
    x = p1.curr_pos
    y = p2.curr_pos
    d = x - y
    return np.sqrt(np.sum(d ** 2))


distances = {}
for from_ in links:
    distances[from_] = {
        m: dist_particles(particles[from_], particles[m]) for m in links[from_]
    }


fig = plt.figure()
camera = Camera(fig)


def draw_lines(particles, links):
    for from_ in links:
        x = particles[from_].curr_pos
        for to_ in links[from_]:
            y = particles[to_].curr_pos
            plt.plot([x[0], y[0]], [x[1], y[1]], "b")


def draw_points(particles):
    for p in particles:
        p.show()


def apply_link_constraints(particles, links, distances):
    for link_pass in range(10):
        for from_ in links:
            p1 = particles[from_]
            for to_ in links[from_]:
                p2 = particles[to_]
                dx = p2.curr_pos - p1.curr_pos
                dist = np.sqrt(np.sum(dx ** 2))
                fraction = ((distances[from_][to_] - dist) / dist) / 2
                dx *= fraction
                p1.curr_pos -= dx
                p2.curr_pos += dx


def apply_boundary_condition(p):
    if p.curr_pos[1] < 0:
        dx = p.compute_dx()
        p.curr_pos[1] = 0  # current pos on ground
        p.prev_pos[1] = dx[1] * 0.5


for timesteps in range(20):

    # particle loop
    for i, p in enumerate(particles):

        p.update_location()

        # check boundary constraint
        apply_boundary_condition(p)

        # link constraints
    apply_link_constraints(particles, links, distances)

    # draw points
    draw_points(particles)

    # draw lines
    draw_lines(particles, links)

    camera.snap()

plt.show()
