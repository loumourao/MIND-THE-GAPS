from typing import Tuple
from random import randrange, uniform
from collidium.geometry import *

def circle_pair(c1: xyz, r1: Real, c2: xyz, r2: Real) -> Tuple[circle, circle]:
    return circle(c1, r1), circle(c2, r2)
    
def first_quadrant_random_circle_pair(min_x: int, max_x: int,
                                      min_y: int, max_y: int,
                                      boundary_delta: int) -> Tuple[circle, circle]:
    c1 = xy(randrange(min_x + boundary_delta, max_x - boundary_delta + 1),
            randrange(min_y + boundary_delta, max_y - boundary_delta + 1))
    r1 = randrange(1, min(c1.cx(), c1.cy(), max_x - c1.cx(), max_y - c1.cy()) + 1)

    c2 = xy(randrange(min_x + boundary_delta, max_x - boundary_delta + 1),
            randrange(min_y + boundary_delta, max_y - boundary_delta + 1))
    r2 = randrange(1, min(c2.cx(), c2.cy(), max_x - c2.cx(), max_y - c2.cy()) + 1)

    return circle_pair(c1, r1, c2, r2)
