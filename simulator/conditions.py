import numpy as np


def apply_boundary_condition(p):
    if p.curr_pos[1] < 0:
        dx = p.compute_dx()
        p.curr_pos[1] = 0  # current pos on ground
        p.prev_pos[1] = dx[1] * 0.5


def apply_link_constraints(
    particles, links, distances, pinned_particles: dict = {}, number_of_passes: int = 5
):
    for _ in range(number_of_passes):
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

                if from_ in pinned_particles:
                    particles[from_].curr_pos = np.array(pinned_particles[from_])
                if to_ in pinned_particles:
                    particles[to_].curr_pos = np.array(pinned_particles[to_])
