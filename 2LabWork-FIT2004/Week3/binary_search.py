"""
Not done
"""
def binary_search(a_list, target):
    """
    Quite a bit more complex than lecture's ver.

    @pre-condition: a_list is sorted (+ a_list has O(1) access time (assume))
    :param a_list:
    :param target:
    :return: index of target in a_list if the target exists. Otherwise, return -1
    """
    low = 0
    high = len(a_list)  # Why
    
    while low < high:  # Why. <= with empty list results in infinite loop // index out of range
        # But can't do this or [0,1,5,6,7,8], [5, 6, 7, 8, 9, 10] will have 5 skipped
        # high and low skip mid when move, mid will be b/w new high and low, since high not checked,
        #   target may be at high
        mid = (low + high) // 2
        if a_list[mid] == target:   # [CROSS] use mid causes infinite loop in list with one target element
            return mid
        elif a_list[mid] < target:
            low = mid   # Why
        else:
            high = mid  # Why
    return -1

target = 5
input_lists = [[],      # empty
               #[5], [1], [9],     # one elem: equal, less, more
               [20, 30, 40, 50, 60],    # Target less than first elem
               [0, 1, 2, 3, 4],     # Target more than last elem
               [0, 1, 2, 3, 4, 5], [0, 1, 5, 6, 7, 8], [5, 6, 7, 8, 9, 10],       # Target is first, middle, last element
               [0, 1, 2, 3, 4, 6]  # Target not in list
               ]
for i in range(len(input_lists)):
    print(binary_search(input_lists[i], target))
