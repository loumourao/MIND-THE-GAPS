from typing import Union
from collidium.geometry.coordinates import *

class circle:
    def __init__(self, center: Union[x, y, xy], radius: Real):
        self.center = center
        self.radius = radius
    
    def get_center(self) -> xyz:
        return self.center
    
    def get_radius(self) -> Real:
        return self.radius
