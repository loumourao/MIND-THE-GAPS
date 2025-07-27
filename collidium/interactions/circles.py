from typing import Tuple
from collidium.geometry import *

def intersects(circle1: circle, circle2: circle) -> bool:
    c1 = circle1.get_center()
    r1 = circle1.get_radius()
    c2 = circle2.get_center()
    r2 = circle2.get_radius()

    return (c2 - c1).magnitude() <= r1 + r2

def closest_points(circle1: circle, circle2: circle) -> Tuple[xyz, xyz]:
    c1 = circle1.get_center()
    r1 = circle1.get_radius()
    c2 = circle2.get_center()
    r2 = circle2.get_radius()
    
    v1 = (c2 - c1).normalize() * r1
    v2 = -v1.normalize() * r2

    return (c1 + v1,
            c2 + v2)

def interpenetration_distance(circle1: circle, circle2: circle) -> Real:
    a, b = closest_points(circle1, circle2)
    distance = -(a - b).magnitude()
    intersects = intersects(circle1, circle2)

    return distance if intersects else -distance
