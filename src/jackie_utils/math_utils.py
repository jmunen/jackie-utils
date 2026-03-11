def moving_average(values, window):
    """Return a simple moving average over a numeric sequence."""
    if window <= 0:
        raise ValueError("Window must be > 0")
    if window > len(values):
        raise ValueError("Window cannot be larger than the input length")
    return [
        sum(values[i:i + window]) / window
        for i in range(len(values) - window + 1)
    ]