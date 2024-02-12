# find max and min in list
def find_max_min(lst):
    """
    This function finds the maximum and minimum values in a list.

    Args:
        lst (list): The input list.

    Returns:
        tuple: A tuple containing the maximum and minimum values in the list.
    """
    if not lst:
        return None

    max_val = min_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


# Example usage
max_v = find_max_min([1, 2, 3, 4, 5])[0]
min_v = find_max_min([1, 2, 3, 4, 5])[1]

print(f"Maximum value: {max_v}")
print(f"Minimum value: {min_v}")
