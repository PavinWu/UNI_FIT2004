"""

"""


def insertion(a_list):
    for i in range(1, len(a_list)):
        j = i
        current = a_list[j]
        while j > 0 and current < a_list[j - 1]:
            a_list[j] = a_list[j - 1]
            j -= 1
        a_list[j] = current

    return True

a_list = [2134,4,5,5,5,7,3,2,9,5]
insertion(a_list)
print(a_list)


                

