my_list = [56,57,12,6,8,21,5,8,89]

def get_smallest_value(list_):
    smallest        = list_[0]
    smallest_index  = 0

    for a in range(1, len(list_)-1):
        if list_[a] < smallest:
            smallest        = list_[a]
            smallest_index  = a

    return list_[smallest_index] #FIXME: wont register "0" as smallest

print(get_smallest_value(my_list))

def selection_sort(list_):
    returnArr = []
    for a in range(len(list_)): #addubg range(len()) fixes the function, but why?
        small = get_smallest_value(list_)
        #books solution is following: returnArr.append(list_.pop(small)), I need to look closer at .pop()
        returnArr.append(small)
        list_.remove(small)

    return returnArr

print(selection_sort(my_list))
