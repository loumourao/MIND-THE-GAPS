import pandas as pd
import matplotlib.pyplot as plt

from collidium import *
from matplotlib.patches import Circle

n = 1000
rows = []
columns = ['x1', 'y1', 'r1', 'x2', 'y2', 'r2', 'intersects']

for n in range(n):
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
df.to_csv('first_quadrant_circles.csv', index=False)

c1 = xy(rows[-1][0], rows[-1][1])
r1 = rows[-1][2]
c2 = xy(rows[-1][3], rows[-1][4])
r2 = rows[-1][5]
intersects = rows[-1][-1]

fig, ax = plt.subplots()
circle1 = Circle((c1.cx(), c1.cy()), r1,
                 edgecolor='b', facecolor='none')
circle2 = Circle((c2.cx(), c2.cy()), r2,
                 edgecolor='r', facecolor='none')
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
plt.title('A pair of circles that ' + ('intersect' if intersects == 1 else 'don\'t intersect'))
plt.savefig('proximity_query.png')
