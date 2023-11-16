def is_positive_number(x):
    return isinstance(x, (int, float)) and x > 0

def is_two_item_list(input_list):
    return isinstance(input_list, list) and len(input_list) == 2

def is_rectangle(input_list):
    return is_two_item_list(input_list) and is_positive_number(input_list[0]) and is_positive_number(input_list[1])

def is_square(input_list):
    def is_rectangle and input_list[0] == input_list[1]

# Tests
"""
print(is_positive_number(5))
print(is_positive_number('foo'))
print(is_positive_number(-1))
print(is_positive_number(0))
"""
