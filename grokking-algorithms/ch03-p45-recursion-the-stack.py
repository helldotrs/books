def get_factorial(x):
    if x == 1:
        return 1
    else:
        return x * get_factorial(x-1)

print(get_factorial(3))
