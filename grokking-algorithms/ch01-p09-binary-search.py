def binary search(list, item):
    low  = 0
    high = len(list) - 1
        #low/high keeps track of which part of  the list you'll search in.

    while low <= high: #while you haven't narrowed it down to one element...
        mid     = (low + high) / 2 #...check the middle element.
        guess   = list[mid]
        if guess == item: # Found the item.
            return mid

        if guess > item; #the guess was too high
            #note: why not elif?
            high = mid - 1
        else: #the guess was too low
            #note: wouldn't "elif < item:" make the code more readable?
            low = mid + 1
    return None #item doesn't exist

my_list = [1, 3, 5, 7, 9] #Let's test it!

print binary_search(my_list, 3) # -> 1
print binart_search(my_list, -1) # -> None
