from __future__ import annotations
from math import sqrt, sin, cos, isclose
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
        return sqrt(self.cx()**2 + \
                    self.cy()**2 + \
                    self.cz()**2)

    def normalize(self) -> vxyz:
        norm = self.magnitude()
        return vxyz(self.cx() / norm,
                    self.cy() / norm,
                    self.cz() / norm)

    def __add__(self, other: vxyz) -> vxyz:
        return vxyz(self.cx() + other.cx(),
                    self.cy() + other.cy(),
                    self.cz() + other.cz())

    def __sub__(self, other: vxyz) -> vxyz:
        return vxyz(self.cx() - other.cx(),
                    self.cy() - other.cy(),
                    self.cz() - other.cz())

    def __mul__(self, other: Real) -> vxyz:
        return vxyz(self.cx() * other,
                    self.cy() * other,
                    self.cz() * other)

    def __neg__(self) -> vxyz:
        return vxyz(-self.cx(),
                    -self.cy(),
                    -self.cz())

    def __eq__(self, other: vxyz) -> bool:
        return isclose(self.cx(), other.cx()) and \
               isclose(self.cy(), other.cy()) and \
               isclose(self.cz(), other.cz())

    def __str__(self) -> str:
        return f"vxyz({self.cx():.2g}, " \
                    f"{self.cy():.2g}, " \
                    f"{self.cz():.2g})"

class vx(vxyz):
    def __init__(self, x: Real) -> vx:
        super().__init__(x, 0, 0)

    def __str__(self) -> str:
        return f"vx({self.cx():.2g})"

class vy(vxyz):
    def __init__(self, y: Real) -> vy:
        super().__init__(0, y, 0)

    def __str__(self) -> str:
        return f"vy({self.cy():.2g})"

class vz(vxyz):
    def __init__(self, z: Real) -> vz:
        super().__init__(0, 0, z)

    def __str__(self) -> str:
        return f"vz({self.cz():.2g})"

class vxy(vxyz):
    def __init__(self, x: Real, y: Real) -> vxy:
        super().__init__(x, y, 0)

    def __str__(self) -> str:
        return f"vxy({self.cx():.2g}, " \
                   f"{self.cy():.2g})"

class vxz(vxyz):
    def __init__(self, x: Real, z: Real) -> vxz:
        super().__init__(x, 0, z)

    def __str__(self) -> str:
        return f"vxz({self.cx():.2g}, " \
                   f"{self.cz():.2g})"

class vyz(vxyz):
    def __init__(self, y: Real, z:Real) -> vyz:
        super().__init__(0, y, z)

    def __str__(self) -> str:
        return f"vyz({self.cy():.2g}, " \
                   f"{self.cz():.2g})"

class vpol(vxyz):
    def __init__(self, rho: Real, theta: Real) -> vpol:
        super().__init__(rho * cos(theta),
                         rho * sin(theta),
                         0)
        self.rho = rho
        self.theta = theta

    def crho(self):
        return self.rho

    def ctheta(self):
        return self.theta

    def __str__(self):
        return f"vpol({self.crho():.2g}, " \
                    f"{self.ctheta():.2g})"
