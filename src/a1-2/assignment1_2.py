from __future__ import annotations

from math import cos, sin
from typing import Any

from fable_modules.fable_library.double import divide
from fable_modules.fable_library.int32 import parse
from fable_modules.fable_library.list import (FSharpList, find, item, iterate,
                                              map, of_array)
from fable_modules.fable_library.range import range_big_int
from fable_modules.fable_library.seq import to_list
from fable_modules.fable_library.string_ import interpolate, printf, to_console
from fable_modules.fable_library.util import create_atom, get_enumerator

# This python code was originally written in F#, and transpiled using Fable.
# Refer to the original source code in the included .fs file if interested :)

# Exercise 1
def odd_and_mod7(n: int) -> str:
    return ((((("" + str(n)) + " is ") + ("even" if ((n % 2) == 0) else "odd")) + " and ") + ("" if ((n % 7) == 0) else "not ")) + "divisible with 7"


to_console(printf("Enter any integer:"))

user_input: str = input()

def _arrow0(__unit: None=None) -> str:
    try: 
        return odd_and_mod7(parse(user_input, 511, False, 32))

    except Exception as _e:
        return "Given invalid input. Please input an integer!"



output: str = _arrow0()

to_console(("" + output) + "")

# Exercise 2
def absolute_diff(a: int, b: int) -> int:
    if a < b:
        return b - a

    else: 
        return a - b



def action(tupled_arg: tuple[int, int]) -> None:
    a: int = tupled_arg[0] or 0
    b: int = tupled_arg[1] or 0
    to_console(((((("Absolute difference between " + str(a)) + " and ") + str(b)) + " is ") + str(absolute_diff(a, b))) + "")


iterate(action, of_array([(2, 4), (4, 2), (69, 0)]))

# Exercise 3
def find_max(a: int, b: int, c: int) -> int:
    if a < b:
        if b < c:
            return c

        else: 
            return b


    elif a < c:
        return c

    else: 
        return a



def find_min(a: int, b: int, c: int) -> int:
    if a < b:
        if c < a:
            return c

        else: 
            return a


    elif c < b:
        return c

    else: 
        return b



def print_largest(a: int, b: int, c: int) -> None:
    to_console(((((((("Amongst " + str(a)) + ", ") + str(b)) + " and ") + str(c)) + ", ") + str(find_max(a, b, c))) + " is the largest")


def print_swapped(a: int, b: int, c: int) -> None:
    min: int = find_min(a, b, c) or 0
    max: int = find_max(a, b, c) or 0
    def mapping(n: int, a: Any=a, b: Any=b, c: Any=c) -> int:
        if n == min:
            return max

        elif n == max:
            return min

        else: 
            return n


    swapped: FSharpList[int] = map(mapping, of_array([a, b, c]))
    to_console(((((((((((("" + str(a)) + ", ") + str(b)) + " and ") + str(c)) + " swapped -> ") + str(item(0, swapped))) + ", ") + str(item(1, swapped))) + " and ") + str(item(2, swapped))) + "")


def print_ascending(a: int, b: int, c: int) -> None:
    min: int = find_min(a, b, c) or 0
    max: int = find_max(a, b, c) or 0
    def predicate(n: int, a: Any=a, b: Any=b, c: Any=c) -> bool:
        if n != max:
            return n != min

        else: 
            return False


    to_console(((((((((((("" + str(a)) + ", ") + str(b)) + " and ") + str(c)) + " ascending -> ") + str(min)) + ", ") + str(find(predicate, of_array([a, b, c])))) + " and ") + str(max)) + "")


def action(tupled_arg: tuple[int, int, int]) -> None:
    a: int = tupled_arg[0] or 0
    b: int = tupled_arg[1] or 0
    c: int = tupled_arg[2] or 0
    print_largest(a, b, c)
    print_swapped(a, b, c)
    print_ascending(a, b, c)


iterate(action, of_array([(2, 4, 5), (5, 2, 4), (4, 5, 2), (5, 4, 2)]))

# Exercise 4
def action(n: int) -> None:
    to_console(("" + odd_and_mod7(n)) + "")


iterate(action, to_list(range_big_int(0, 1, 50)))

# ...and with loop
with get_enumerator(to_list(range_big_int(0, 1, 50))) as enumerator:
    while enumerator.System_Collections_IEnumerator_MoveNext():
        to_console(("With for loop: " + odd_and_mod7(enumerator.System_Collections_Generic_IEnumerator_1_get_Current())) + "")

# Exercise 5
def action(k: float) -> None:
    to_console(interpolate("%.2f%P()", [divide(cos(k), sin(k))]))


def mapping(value: int) -> float:
    return value


iterate(action, map(mapping, to_list(range_big_int(1, 1, 40))))

# ...with for loop (in F# anyways...)
with get_enumerator(to_list(range_big_int(1, 1, 40))) as enumerator:
    while enumerator.System_Collections_IEnumerator_MoveNext():
        k: float = enumerator.System_Collections_Generic_IEnumerator_1_get_Current()
        to_console(interpolate("With for loop: %.2f%P()", [divide(cos(k), sin(k))]))

# ...and with while loop
i: int = create_atom(1)

while i() >= 40:
    k: float = i()
    to_console(interpolate("With while loop: %.2f%P()", [divide(cos(k), sin(k))]))
    i(i() + 1)

