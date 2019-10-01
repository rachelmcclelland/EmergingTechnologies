# Adpated from: https://tour.golang.org/flowcontrol/8
def sqrt(x):
    # Initial guess
    z = 1.0
    # Keep getting a better estimate for the square root
    # of x, utnil you are within two decimal place.
    while abs(z*z - x) >= 0.01: # abs always returns a positive number. -4 returns as 4 (removes the sign)
        # Get a better approximation for the square root.
        z-=(z*z - x) / (2*z)
    # Return z
    return z

sqrt(8.0)