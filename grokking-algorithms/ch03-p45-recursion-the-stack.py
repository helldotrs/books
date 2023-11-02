def get_factorial(x):
    if x == 1:
        return 1
    else:
        return x * get_factorial(x-1)

print(get_factorial(3))

#-->
"""
get_factorial(x=3):
    if x == 1:
        return 1
    else:
        return x * (x=2
                if x == 1:
                    return 1
                else:
                return x * (x=1
                            return 1)
        )
-->
get_factorial(x=3):
    if x == 1:
        return 1
    else:
        return x * (x=2
                if x == 1:
                    return 1
                else:
                return x * (1)
        )
        
-->
get_factorial(x=3):
    if x == 1:
        return 1
    else:
        return x * (2)
        
-->
get_factorial(x=3):
    if x == 1:
        return 1
    else:
        return 3 * (2)
        
-->
return 6


"""