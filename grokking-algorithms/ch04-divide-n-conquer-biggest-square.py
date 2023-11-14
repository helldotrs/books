def validate_input(input_list):
    # Check if input_list is a list
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")

    # Check if the list has exactly two elements
    if len(input_list) != 2:
        raise ValueError("List must contain exactly two elements")

    # Check if both elements are either positive integers or floats
    for element in input_list:
        if not isinstance(element, (int, float)) or element <= 0:
            raise ValueError("Elements in the list must be positive integers or floats")

# Example usage:
try:
    validate_input([3, 4.5])
    print("Input is valid.")
except ValueError as e:
    print(f"Error: {e}")
