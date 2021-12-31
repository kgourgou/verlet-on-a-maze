import matplotlib.pyplot as plt


def draw_lines(particles: dict, links: dict):
    for from_ in links:
        try:
            x = particles[from_].curr_pos
            for to_ in links[from_]:
                y = particles[to_].curr_pos
                plt.plot([x[0], y[0]], [x[1], y[1]], "b")
        except KeyError:
            continue


def draw_points(particles: dict):
    for p in particles.values():
        p.show()
