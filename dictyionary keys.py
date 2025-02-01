def generate_squares(start, end):
    """
    Generate a dictionary of squares for numbers in the given range.
    
    :param start: Starting number (inclusive)
    :param end: Ending number (inclusive)
    :return: Dictionary with numbers as keys and their squares as values
    """
    if start > end:
        raise ValueError("Start value must be less than or equal to end value.")
    return {x: x ** 2 for x in range(start, end + 1)}

# we can then use an example below to test this logic
try:
    d = generate_squares(1, 20)
    print(d)
except ValueError as e:
    print(f"Error: {e}")
