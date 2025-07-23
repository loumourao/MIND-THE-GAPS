from __future__ import annotations
from functools import singledispatchmethod
from math import sqrt
from numbers import Real

class vxyz:
    def __init__(self, x: Real, y: Real, z: Real) -> vxyz:
        self.x = x
        self.y = y
        self.z = z

    def cx(self) -> Real:
        return self.x
    
    def cy(self) -> Real:
        return self.y
    
    def cz(self) -> Real:
        return self.z
    
    def magnitude(self) -> Real:
        return sqrt(self.cx()**2 + self.cy()**2 + self.cz()**2)
    
    @singledispatchmethod
    def __add__(self, other: vxyz) -> vxyz:
        return vxyz(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z)
    
    @singledispatchmethod
    def __sub__(self, other: vxyz) -> vxyz:
        return vxyz(self.x - other.x,
                    self.y - other.y,
                    self.z - other.z)

    @singledispatchmethod
    def __mul__(self, other: Real) -> vxyz:
        return vxyz(self.x * other,
                    self.y * other,
                    self.z * other)

class vx(vxyz):
    def __init__(self, x: Real) -> vxyz:
        super().__init__(x, 0, 0)

class vy(vxyz):
    def __init__(self, y: Real) -> vxyz:
        super().__init__(0, y, 0)

class vz(vxyz):
    def __init__(self, z: Real) -> vxyz:
        super().__init__(0, 0, z)

class vxy(vxyz):
    def __init__(self, x: Real, y: Real) -> vxyz:
        super().__init__(x, y, 0)

class vxz(vxyz):
    def __init__(self, x: Real, z: Real) -> vxyz:
        super().__init__(x, 0, z)

class vyz(vxyz):
    def __init__(self, y: Real, z:Real) -> vxyz:
        super().__init__(0, y, z)
