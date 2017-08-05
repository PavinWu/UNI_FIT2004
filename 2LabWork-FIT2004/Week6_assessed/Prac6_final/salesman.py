def salesman():
    f = open('houses.txt', 'r')
    N = int(f.readline())    # number of houses in street
    price_list = f.readline().split()   # this contains strings! We typecast one by one to make code compact

    k = 3   # specify neighbour range
    
    ## FIND SOLUTION STEP
    partial_max_prices = [int(price_list[0])]    
    max_past_soln = 0
    for i in range(1, len(price_list)):    # house number - 1 (since house starts from 1)
        if (i - k) <= 0:                    # before any house beyond the 'neighbourhood' perimeter is available
            partial_max_prices.append(int(price_list[i]))
        else:
            if partial_max_prices[i - k - 1] > max_past_soln:    # if of all past max, this new price at i-k is greater  (sub-soln to sub-soln)
                max_past_soln = int(partial_max_prices[i - k - 1])
            partial_max_prices.append(int(price_list[i]) + max_past_soln)
    max_past_soln = max(partial_max_prices)     # max_past_soln is of index before i-k. We update it here for all i.
    
    ## BACKTRACK STEP
    sub_max_soln = max_past_soln
    i = len(partial_max_prices) - 1
    houses = []  
    while i >= 0:
        if partial_max_prices[i] == sub_max_soln:   # want to find which index gives max
            houses.append(i + 1)    # house number starts from 1
            sub_max_soln -= int(price_list[i])  # take off from original price (in index which gives max)
        i -= 1
    
    return reverse(houses), max_past_soln
    
def reverse(list):  # we need this simply because we search houses from last element
    l = len(list)-1
    for i in range(len(list)//2):
        list[i], list[l-i] = list[l-i],list[i]
    return list
    
if __name__ == "__main__":
    print("Houses: " + str(salesman()[0]).strip('[]').replace(',', ''))
    print("Total sale: " + str(salesman()[1]))
    
    