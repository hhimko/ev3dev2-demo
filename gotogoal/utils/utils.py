from typing import Union


# generic type for real numbers
# this line can be replaced with `Numeric = int | float` in Python 3.10
Numeric = Union[int, float]

def clamp(val, *, lower: Numeric, upper: Numeric) -> Numeric:
    return max(lower, min(upper, val))