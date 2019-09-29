# The number we will perform the collatz operations on.

n = int(input("Enter a positive integer: "))

# Keep looping until we reach one
# Note: this assumes the Collatz conjecture is true
while n != 1:
    # Print the value of n
    print(n)

    # Check if n is even
    if n % 2 == 0:
        # If n is even, divide by 2
        n = n // 2 # What is difference between / and //?
    else:
        # If n is odd, mulitply by three and add 1
        n = (3 * n) + 1

# Finally, print the 1
print(n)