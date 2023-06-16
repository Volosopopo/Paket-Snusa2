def multiple_of_index(arr):
    return [num for i, num in enumerate(arr) if i != 0 and num % i == 0 or i == num]