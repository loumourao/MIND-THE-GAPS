from collidium.geometry import *

def intersects(circle1: circle, circle2: circle) -> bool:
    c1 = circle1.get_center()
    r1 = circle1.get_radius()
    c2 = circle2.get_center()
    r2 = circle2.get_radius()
    return (c2 - c1).magnitude() <= r1 + r2
