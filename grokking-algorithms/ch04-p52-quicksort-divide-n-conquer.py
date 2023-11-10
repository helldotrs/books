plot = [1680, 640]

# FIXME: rewrite to use recursion instead of while loop

def biggest_square(array):
    x = plot[0]
    y = plot[1]

    while(x != y):
        if x < y:
            y / 2
        elif (x > y):
            x / 2
        else:
            return [x, y]
    
    return [0, 0]

print(biggest_square(plot))
