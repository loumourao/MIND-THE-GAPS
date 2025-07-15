from typing import Union
from coordinates import *

class circle:
    def __init__(self, center: Union[x, y, xy], radius: Real):
        self.center = center
        self.radius = radius
    
    def get_center(self) -> xyz:
        return self.c
    
    def get_radius(self) -> Real:
        return self.r
