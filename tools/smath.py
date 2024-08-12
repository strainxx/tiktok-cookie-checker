def clamp(min: int, max: int, val: int):
    if val < min: return min
    if val > max: return max
    return val