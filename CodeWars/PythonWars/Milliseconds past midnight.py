# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    hours = h * 3_600_000
    minutes = m * 60_000
    seconds = s * 1000

    return hours + minutes + seconds
