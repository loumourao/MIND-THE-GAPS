import math
import pandas as pd
import matplotlib.pyplot as plt

from collidium.geometry import *
from collidium.interactions import *
from collidium.generative_functions import *
from matplotlib.patches import Circle

# Not a big fan of this function... A much more clever way of managing interesection distributions should be considered (generative_functions itself)
def circles_proximity_queries_dataset_generator(n: Real, intersection_distribution: Real, file_name: str) -> None:
    rows = []
    columns = ['x1', 'y1', 'r1', 'x2', 'y2', 'r2', 'intersects']
    n_intersects = math.ceil(n * intersection_distribution)
    n_no_intersects = math.ceil(n * (1 - intersection_distribution))

    for _ in range(n_intersects):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        while not intersects(circle1, circle2):
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

    for _ in range(n_no_intersects):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        while intersects(circle1, circle2):
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

# Not a big fan of this function... (Same as before)
# Plus: I should think of a generalizable dataset_generator that takes dynamic columns and values as such generators are expected to scale...
def circles_interpenetration_distance_dataset_generator(n: Real, intersection_distribution: Real, file_name: str) -> None:
    rows = []
    columns = ['x1', 'y1', 'r1', 'x2', 'y2', 'r2', 'interpenetration_distance']
    n_intersects = math.ceil(n * intersection_distribution)
    n_no_intersects = math.ceil(n * (1 - intersection_distribution))

    for _ in range(n_intersects):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        while not intersects(circle1, circle2):
            circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                                 0, 100,
                                                                 1)

        c1 = circle1.get_center()
        r1 = circle1.get_radius()
        c2 = circle2.get_center()
        r2 = circle2.get_radius()
        inter_depth = interpenetration_distance(circle1, circle2)

        rows.append([c1.x, c1.y, r1,
                     c2.x, c2.y, r2,
                     inter_depth])

    for _ in range(n_no_intersects):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        while intersects(circle1, circle2):
            circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                                 0, 100,
                                                                 1)

        c1 = circle1.get_center()
        r1 = circle1.get_radius()
        c2 = circle2.get_center()
        r2 = circle2.get_radius()
        inter_depth = interpenetration_distance(circle1, circle2)

        rows.append([c1.x, c1.y, r1,
                     c2.x, c2.y, r2,
                     inter_depth])

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(file_name, index=False)

# Not a big fan of this function... (Same as before)
def circles_closest_points_dataset_generator(n: Real, intersection_distribution: Real, file_name: str) -> None:
    rows = []
    columns = ['x1', 'y1', 'r1', 'x2', 'y2', 'r2', 'ax', 'ay', 'bx', 'by']
    n_intersects = math.ceil(n * intersection_distribution)
    n_no_intersects = math.ceil(n * (1 - intersection_distribution))

    for _ in range(n_intersects):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        while not intersects(circle1, circle2):
            circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                                 0, 100,
                                                                 1)

        c1 = circle1.get_center()
        r1 = circle1.get_radius()
        c2 = circle2.get_center()
        r2 = circle2.get_radius()
        a, b = closest_points(circle1, circle2)

        rows.append([c1.x, c1.y, r1,
                     c2.x, c2.y, r2,
                     a.x, a.y,
                     b.x, b.y])

    for _ in range(n_no_intersects):
        circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                             0, 100,
                                                             1)

        while intersects(circle1, circle2):
            circle1, circle2 = first_quadrant_random_circle_pair(0, 100,
                                                                 0, 100,
                                                                 1)

        c1 = circle1.get_center()
        r1 = circle1.get_radius()
        c2 = circle2.get_center()
        r2 = circle2.get_radius()
        a, b = closest_points(circle1, circle2)

        rows.append([c1.x, c1.y, r1,
                     c2.x, c2.y, r2,
                     a.x, a.y,
                     b.x, b.y])

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(file_name, index=False)

def proximity_query_random_figure_generator(dataset_file_name: str) -> None:
    df = pd.read_csv(dataset_file_name)
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

def interpenetration_distance_random_figure_generator(dataset_file_name: str) -> None:
    df = pd.read_csv(dataset_file_name)
    row = df.sample(n=1).values.tolist()[0]

    c1 = xy(row[0], row[1])
    r1 = row[2]
    c2 = xy(row[3], row[4])
    r2 = row[5]
    inter_depth = row[-1]

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
    plt.title(f'A pair of circles with an interpenetration distance of {inter_depth:.2g}')
    plt.savefig('interpenetration_distance.png')

def closest_points_random_figure_generator(dataset_file_name: str) -> None:
    df = pd.read_csv(dataset_file_name)
    row = df.sample(n=1).values.tolist()[0]

    c1 = xy(row[0], row[1])
    r1 = row[2]
    c2 = xy(row[3], row[4])
    r2 = row[5]
    a = xy(row[6], row[7])
    b = xy(row[8], row[9])

    circle1 = Circle((c1.cx(), c1.cy()), r1,
                     edgecolor='b', facecolor='none', zorder=1)
    circle2 = Circle((c2.cx(), c2.cy()), r2,
                     edgecolor='r', facecolor='none', zorder=1)

    _, ax = plt.subplots()
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.plot([a.x, b.x], [a.y, b.y],
            color='m', zorder=2)
    ax.plot(a.x, a.y,
            marker='o', markeredgecolor='k', markerfacecolor='y',
            markersize=3, zorder=3)
    ax.plot(b.x, b.y,
            marker='o', markeredgecolor='k', markerfacecolor='c',
            markersize=3, zorder=3)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    plt.title(f'A pair of circles with closest points A({a.x:.2g}, {a.y:.2g}) and B({b.x:.2g}, {b.y:.2g})')
    plt.savefig('closest_points.png')
