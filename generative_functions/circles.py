from typing import Tuple
from sys import maxsize, float_info
from random import randrange, uniform
from geometry import *

def circle_pair(c1: xyz, r1: Real, c2: xyz, r2: Real) -> Tuple[circle, circle]:
    return circle(c1, r1), circle(c2, r2)
    
def random_circle_pair(min_x: int, max_x: int, min_y: int, max_y: int) -> Tuple[circle, circle]:
    c1 = xy(randrange(min_x, max_x),
            randrange(min_y, max_y))
    r1 = randrange()

    c2 = xy(randrange(min_x, max_x),
            randrange(min_y, max_y))
    r2 = randrange()

    return circle(c1, r1), circle(c2, r2)

def random_circle_pair(min_x: Real, max_x: Real, min_y: Real, max_y: Real) -> Tuple[circle, circle]:
    return None

def random_integer_first_quadrant_circle_pair() -> Tuple[circle, circle]:
    return random_circle_pair(0, maxsize, 0, maxsize)

def random_float_first_quadrant_circle_pair() -> Tuple[circle, circle]:
    return random_circle_pair(0.0, float_info.max, 0.0, float_info.max)
