def find_miss_inv_cal(invoice_set):
    """
    Find missing invoice in O(1) space and O(N) time complexity
    """
    f = open(invoice_set, 'r')
    N_k = f.readline()
    N_k = N_k.split()
    N = int(N_k[0])
    k = int(N_k[1])
    
    if k != 1:  # Assume only one invoice missing
        print("More than one missing invoices!")
        return False
    
    sum_inv = 0     # sum of all invoice numbers
    for line in f:      # This takes O(N) time, O(1) space
        sum_inv += int(line)
        
    ideal_sum_inv = N*(N+1)/2   # ideal sum (if no invoice missing)
    
    miss_inv = ideal_sum_inv - sum_inv

    #f = open('invoice_miss2.txt', 'w')
    print(miss_inv)
    #f.write(str(miss_inv))
    #f.close()
    
    return True

find_miss_inv_cal("testdata2.txt")
