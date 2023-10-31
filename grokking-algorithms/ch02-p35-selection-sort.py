my_list = [2,56,1,57,12,6,8,21,3,5,8,1,2,89,0,]

def get_smallest_value(list_):
    smallest        = list_[0]
    smallest_index  = 0

    for a in range(1, len(list_)-1):
        if list_(a) < smallest:
            smallest        = list_[a]
            smallest_index  = a

    return list_[smallest_index]

print(get get_smallest_value(my_list))
