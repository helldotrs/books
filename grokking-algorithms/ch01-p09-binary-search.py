def binary_search(input_list, item):
    low  = 0
    high = len(input_list) - 1
        #low/high keeps track of which part of  the input_list you'll search in.

    while low <= high: #while you haven't narrowed it down to one element...
        mid     = int((low + high) / 2) #...check the middle element.
            #NOTE: int() missing in the book, returning a float. can be fixed either with int(x/2) OR x//2, I think the first solution is a bit clearer
        guess   = input_list[mid]
        if guess == item: # Found the item.
            return mid

        if guess > item: #the guess was too high
            #note: why not elif?
            high = mid - 1
        else: #the guess was too low
            #note: wouldn't "elif < item:" make the code more readable?
            low = mid + 1
    return None #item doesn't exist

my_list = [1, 3, 5, 7, 9] #Let's test it!

print(binary_search(my_list, 3)) # -> 1
print(binary_search(my_list, -1)) # -> None

