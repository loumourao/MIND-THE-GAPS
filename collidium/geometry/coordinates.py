from __future__ import annotations
from numbers import Real
from math import sin, cos, isclose
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
        return isclose(self.cx(), other.cx()) and \
               isclose(self.cy(), other.cy()) and \
               isclose(self.cz(), other.cz())

    def __str__(self) -> str:
        return f"xyz({self.cx():.2g}, " \
                   f"{self.cy():.2g}, " \
                   f"{self.cz():.2g})"

class x(xyz):
    def __init__(self, x: Real) -> x:
        super().__init__(x, 0, 0)

    def __str__(self) -> str:
        return f"x({self.cx():.2g})"

class y(xyz):
    def __init__(self, y: Real) -> y:
        super().__init__(0, y, 0)

    def __str__(self) -> str:
        return f"y({self.cy():.2g})"

class z(xyz):
    def __init__(self, z: Real) -> z:
        super().__init__(0, 0, z)

    def __str__(self) -> str:
        return f"z({self.cz():.2g})"

class xy(xyz):
    def __init__(self, x: Real, y: Real) -> xy:
        super().__init__(x, y, 0)

    def __str__(self) -> str:
        return f"xy({self.cx():.2g}, " \
                  f"{self.cy():.2g})"

class xz(xyz):
    def __init__(self, x: Real, z: Real) -> xz:
        super().__init__(x, 0, z)

    def __str__(self) -> str:
        return f"xz({self.cx():.2g}, " \
                  f"{self.cz():.2g})"

class yz(xyz):
    def __init__(self, y: Real, z: Real) -> yz:
        super().__init__(0, y, z)

    def __str__(self) -> str:
        return f"yz({self.cy():.2g}, " \
                  f"{self.cz():.2g})"

class pol(xyz):
    def __init__(self, rho: Real, theta: Real) -> pol:
        super().__init__(rho * cos(theta),
                         rho * sin(theta),
                         0)
        self.rho = rho
        self.theta = theta

    def crho(self) -> Real:
        return self.rho

    def ctheta(self) -> Real:
        return self.theta

    def __str__(self) -> str:
        return f"pol({self.crho():.2g}, " \
                   f"{self.ctheta():.2g})"
