# Create an empty dictionary 'd' to store the squares of numbers.
d = dict()

# Iterate through numbers from 1 to 20 (inclusive).
for x in range(1, 21):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x ** 2

# Print the dictionary 'd' containing the squares of numbers from 1 to 20.
print(d)
