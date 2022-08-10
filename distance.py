# A program that provides a falling distance in meters.
# Using d=1/2ft**2 equation.

# Set the constant
GRAVITY = 9.8


def falling_distance(time):

    distance = float(1/2*GRAVITY)*(time**2)

    return distance
