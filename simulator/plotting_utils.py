import matplotlib.pyplot as plt


def draw_lines(particles, links):
    for from_ in links:
        x = particles[from_].curr_pos
        for to_ in links[from_]:
            y = particles[to_].curr_pos
            plt.plot([x[0], y[0]], [x[1], y[1]], "b")


def draw_points(particles):
    for p in particles:
        p.show()
