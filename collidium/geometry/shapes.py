from collidium.geometry.coordinates import *

class circle:
    def __init__(self, center: xyz, radius: Real):
        self.center = center
        self.radius = radius

    def get_center(self) -> xyz:
        return self.center

    def get_radius(self) -> Real:
        return self.radius

    def __str__(self) -> str:
        return f"Circle(center: {self.get_center()},\
                        radius: {self.get_radius():.2g})"
