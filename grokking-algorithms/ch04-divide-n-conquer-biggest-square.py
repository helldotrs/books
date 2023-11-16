def is_positive_number(x):
    if not isinstance(value, (int, float)) or value <= 0:
        exit("must be positive number")

#test
is_positive_number(5)
is_positive_number('foo')
is_positive_number(-1)
is_positive_number(0)
