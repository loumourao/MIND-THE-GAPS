from functools import singledispatchmethod
from __future__ import annotations
from numbers import Real
from vectors import vxyz

class xyz:
    def __init__(self, x: Real, y: Real, z: Real) -> xyz:
        self.x = x
        self.y = y
        self.z = z

    def cx(self) -> Real:
        return self.x

    def cy(self) -> Real:
        return self.y

    def cz(self) -> Real:
        return self.z
    
    @singledispatchmethod
    def __sub__(self, other: xyz) -> vxyz:
        return vxyz(self.cx() - other.cx(),
                    self.cy() - other.cy(),
                    self.cz() - other.cz())
        
class x(xyz):
    def __init__(self, x: Real) -> xyz:
        super().__init__(x, 0, 0)

class y(xyz):
    def __init__(self, y: Real) -> xyz:
        super().__init__(0, y, 0)

class z(xyz):
    def __init__(self, z: Real) -> xyz:
        super().__init__(0, 0, z)

class xy(xyz):
    def __init__(self, x: Real, y: Real) -> xyz:
        super().__init__(x, y, 0)

class xz(xyz):
    def __init__(self, x: Real, z: Real) -> xyz:
        super().__init__(x, 0, z)

class yz(xyz):
    def __init__(self, y: Real, z: Real) -> xyz:
        super().__init__(0, y, z)
