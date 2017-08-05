def salesman():
    f = open('houses.txt', 'r')
    N = int(f.readline())    # number of houses in street
    price_list = f.readline().split()   # this contains strings! We typecast one by one to make code compact

    k = 3   # specify neighbour range
    
    ## FIND SOLUTION STEP
    partial_max_prices = [int(price_list[0])]    # max price list (A solution is obtained 
        # --after checking for requirements and constraints-- from smaller solutions in earlier entry)
    # But since we can also keep the overall solution to just the last one before current, we don't need to check all
    max_past_soln = 0
    for i in range(1, len(price_list)):    # house number - 1 (since house starts from 1)
        if (i - k) <= 0:        # before any house beyond the 'neighbourhood' perimeter is available
            partial_max_prices.append(int(price_list[i]))
        else:
            if partial_max_prices[i - k - 1] > max_past_soln:    # if of all past max, this new price at i-k is greater  (sub-soln to sub-soln)
                # we don't take the one at i - k (still neighbour)
                max_past_soln = int(partial_max_prices[i - k - 1])
            partial_max_prices.append(int(price_list[i]) + max_past_soln)
    max_past_soln = max(partial_max_prices)     # max_past_soln is of index before i-k. We update it here for all i.
    
    ## BACKTRACK STEP
    # max is not necessarily in the last entry
    # But since dynamic programming depends on past solutions, the constituents of current solution are solely
    # made up of past solutions, which always come from the entry less than the current one. 
    # i.e. we don't have to worry that any partial solutions will come after than the current max one.
    sub_max_soln = max_past_soln
    i = len(partial_max_prices) - 1
    houses = []     # houses to visit for optimal sales
    while i >= 0:
        if partial_max_prices[i] == sub_max_soln:   # want to find which index gives max
            houses.append(i + 1)    # house number starts from 1
            sub_max_soln -= int(price_list[i])  # take off from original price (in index which gives max)
        i -= 1
    # Notice here that i goes backwards ONLY. This means the number of houses extracted from backtracking will
    # be in descending order ONLY.
    return reverse(houses), max_past_soln
    
    # you reach the end of loop when i < 0 (i.e. last difference is in 0th entry) 
        # or difference reaches 0 during i > 0 (i.e. stays 0 with no partial_max_prices to match until i < 0))
        # (note: entries in partial_max_prices will always be greater than 0. Given that price inputs are 
        # greater than zero. This is because we first set it to zero. Then we will definitely change it to some 
        # prices after some point.
    
def reverse(list):
    l = len(list)-1
    for i in range(len(list)//2):
        list[i], list[l-i] = list[l-i],list[i]
    return list
    
if __name__ == "__main__":
    print("Houses: " + str(salesman()[0]).strip('[]').replace(',', ''))
    print("Total sale: " + str(salesman()[1]))
    
    