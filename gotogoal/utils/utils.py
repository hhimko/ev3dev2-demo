from math import atan2, sin, cos


def clamp(val, /, *, lower: float, upper: float) -> float:
    return max(lower, min(upper, val))


def radians_normalize(rad: float, /) -> float:
    ''' Normalizes an angle in radians to the [-PI, PI] range. '''
    
    return atan2(sin(rad), cos(rad))