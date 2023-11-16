def is_positive_number(x):
    if not isinstance(x, (int, float)) or x <= 0:
        exit("must be positive number")
    return x
"""
#tests
print(is_positive_number(5))
print(is_positive_number('foo'))
print(is_positive_number(-1))
print(is_positive_number(0))
"""
