from __future__ import annotations
from collidium.geometry.coordinates import *

class circle:
    def __init__(self, center: xyz, radius: Real) -> circle:
        self.center = center
        self.radius = radius

    def get_center(self) -> xyz:
        return self.center

    def get_radius(self) -> Real:
        return self.radius

    def __str__(self) -> str:
        return f"Circle(center: {self.get_center()}, " \
                      f"radius: {self.get_radius():.2g})"

class ellipse:
    def __init__(self, center: xyz, a: Real, b: Real, theta: Real) -> ellipse:
        self.center = center
        self.a = a
        self.b = b
        self.theta = theta

    def get_center(self) -> xyz:
        return self.center

    def get_a(self) -> Real:
        return self.a

    def get_b(self) -> Real:
        return self.b

    def get_theta(self) -> Real:
        return self.theta

    def __str__(self) -> str:
        return f"Ellipse(center: {self.get_center()}, " \
                            f"a: {self.get_a():.2g}, " \
                            f"b: {self.get_b():.2g}, " \
                        f"theta: {self.get_theta():.2g})"
