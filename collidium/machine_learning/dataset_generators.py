import pandas as pd
import matplotlib.pyplot as plt

from collidium import *
from matplotlib.patches import Circle

def circles_proximity_queries_dataset_generator(n, file_name):
    rows = []
    columns = ['x1', 'y1', 'r1', 'x2', 'y2', 'r2', 'intersects']

    for _ in range(n):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        c1 = circle1.get_center()
        r1 = circle1.get_radius()
        c2 = circle2.get_center()
        r2 = circle2.get_radius()
        pq = 1 if intersects(circle1, circle2) else 0

        rows.append([c1.x, c1.y, r1,
                     c2.x, c2.y, r2,
                     pq])

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(file_name, index=False)

def random_figure_generator(file):
    df = pd.read_csv(file)
    row = df.sample(n=1).values.tolist()[0]

    c1 = xy(row[0], row[1])
    r1 = row[2]
    c2 = xy(row[3], row[4])
    r2 = row[5]
    intersects = row[-1]

    circle1 = Circle((c1.cx(), c1.cy()), r1,
                     edgecolor='b', facecolor='none')
    circle2 = Circle((c2.cx(), c2.cy()), r2,
                     edgecolor='r', facecolor='none')

    _, ax = plt.subplots()
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    plt.title('A pair of circles that ' + ('intersect' if intersects == 1 else 'don\'t intersect'))
    plt.savefig('proximity_query.png')
