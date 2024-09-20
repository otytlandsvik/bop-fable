from __future__ import annotations

from collections.abc import Callable
from math import pow

from fable_modules.fable_library.double import sqrt
from fable_modules.fable_library.list import iterate, of_array
from fable_modules.fable_library.string_ import interpolate, to_console

# This python code was originally written in F#, and transpiled using Fable.
# Refer to the original source code in the included .fs file if interested :)

# Exercise 1
a: int = 3

to_console(("" + str(a)) + "")


# Exercise 2
def get_abs(f: float) -> float:
    if f < 0.0:
        return f * -1.0

    else:
        return f


to_console(interpolate("Absolute value of %f%P(): %f%P()", [3.0, get_abs(3.0)]))

to_console(interpolate("Absolute value of %f%P(): %f%P()", [-9.0, get_abs(-9.0)]))


# Exercise 3
def bus_ticket_price(age: int) -> None:
    to_console(
        (
            (("Person of age " + str(age)) + " must pay ")
            + str(20 if (age < 18) else (40 if (age < 76) else 30))
        )
        + "kr"
    )


def _arrow0(age: int) -> None:
    bus_ticket_price(age)


iterate(_arrow0, of_array([4, 17, 18, 69, 76, 99]))


# Exercise 4
def euclidean(p1_: float, p1__1: float, p2_: float, p2__1: float) -> float:
    p1: tuple[float, float] = (p1_, p1__1)
    p2: tuple[float, float] = (p2_, p2__1)
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


def _arrow1(__unit: None = None) -> float:
    tupled_arg: tuple[float, float] = (2.0, 2.0)
    tupled_arg_1: tuple[float, float] = (-3.0, -1.0)
    return euclidean(tupled_arg[0], tupled_arg[1], tupled_arg_1[0], tupled_arg_1[1])


distance: float = _arrow1()

to_console(
    interpolate("Eclidean distance between (2, 2) and (-3, -1) is %f%P()", [distance])
)


# Exercise 5
def get_velocity(v0: float, a_1: float, t: float) -> float:
    return v0 + (a_1 * t)


def _arrow2(t: float) -> float:
    return get_velocity(5, 2, t)


velocity_at_time: Callable[[float], float] = _arrow2


def action(t: float) -> None:
    to_console(
        interpolate("Velocity at %.2f%P() was %.2f%P()", [t, velocity_at_time(t)])
    )


iterate(action, of_array([0.0, 4.0, 9.5]))
