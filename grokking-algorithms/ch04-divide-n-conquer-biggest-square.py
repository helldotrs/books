def is_positive_number(x):
    if not isinstance(value, (int, float)) or value <= 0:
        exit("must be positive number")
    return x

#test
print(is_positive_number(5))
print(is_positive_number('foo'))
print(is_positive_number(-1))
print(is_positive_number(0))
