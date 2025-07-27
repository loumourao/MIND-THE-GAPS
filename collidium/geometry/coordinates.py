from __future__ import annotations
from numbers import Real
from collidium.geometry.vectors import vxyz

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

    def __add__(self, other: vxyz) -> xyz:
        return xyz(self.cx() + other.cx(),
                   self.cy() + other.cy(),
                   self.cz() + other.cz())

    def __sub__(self, other: xyz) -> vxyz:
        return vxyz(self.cx() - other.cx(),
                    self.cy() - other.cy(),
                    self.cz() - other.cz())

    def __eq__(self, other: xyz) -> bool:
        return self.cx() == other.cx() and \
               self.cy() == other.cy() and \
               self.cz() == other.cz()

    def __str__(self) -> str:
        return f"xyz({self.cx():.2g}, \
                     {self.cy():.2g}, \
                     {self.cz():.2g})"

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
