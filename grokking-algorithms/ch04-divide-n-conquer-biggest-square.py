def is_positive_number(x):
    if not isinstance(x, (int, float)) or x <= 0:
        return False
    return True

def is_two_item_list(input_list):
    if not isinstance(input_list, list) or  len(input_list) != 2:
        return False
    return True
    
def is_rectangle(input_list):
    if not is_two_item_list(input_list) and is_positive_number(input_list[0]) and is_positive_number(input_list[1]):
        return False
    return True
"""
#tests
print(is_positive_number(5))
print(is_positive_number('foo'))
print(is_positive_number(-1))
print(is_positive_number(0))
"""
