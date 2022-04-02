def clamp(val, /, *, lower: float, upper: float) -> float:
    return max(lower, min(upper, val))