from tqdm import tqdm
import seaborn as sns

from simulator.plotting_utils import draw_lines, draw_points
from simulator.conditions import (
    apply_boundary_condition,
    apply_link_constraints,
)


def simulate(
    particles,
    links,
    PINNED_PARTICLES,
    initial_link_distances,
    camera,
    number_of_passes=3,
    number_of_steps=100,
):
    NUMBER_OF_TIMESTEPS = number_of_steps
    for _ in tqdm(range(NUMBER_OF_TIMESTEPS)):
        # draw points
        draw_points(particles)

        # draw lines
        draw_lines(particles, links)
        sns.despine()
        camera.snap()

        # particle loop
        for i, p in enumerate(particles.values()):
            p.update_location()

            # check boundary constraint
            apply_boundary_condition(p)

        # link constraints
        apply_link_constraints(
            particles,
            links,
            initial_link_distances,
            pinned_particles=PINNED_PARTICLES,
            number_of_passes=number_of_passes,
        )
