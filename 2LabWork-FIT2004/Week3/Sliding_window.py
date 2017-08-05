def sliding_window(a_list, w):
    smooth_list = []
    l = len(a_list)     #have to put here since its length will change after append
    last = a_list[len(a_list) - 1]
    for i in range(w - 1):  # For sum with last element: -1 cuz already have one above
        a_list.append(last)
  
    for k in range(l):
        sum_num = 0
        for j in range(w):
            sum_num += a_list[k + j]
        smooth_list.append(sum_num//w)

    return smooth_list

print(sliding_window([1,2,3,4,7,9, 10, 11, 12, 13], 4))
