# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and
# returns it in cm per second, rounded down to the integer (= floored).

def cockroach_speed(s):
    # km = 100000cm
    # 1km per hour = 100_000cm per hour
    # 1666.67 cm per minute
    # 27.778 cm per second

    speed = s * 100_000
    cmspeed = ((speed / 60) / 60)
    return int(cmspeed)
