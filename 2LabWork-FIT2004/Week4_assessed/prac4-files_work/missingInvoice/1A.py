def find_miss_inv_pp(invoice_set):
    """
    Find missing invoices in O(N) space & O(N) time complexity
    Can't use insertion sort since it will make O(N^2) (even with one input at a time)
    
    @pre-condition: invoice starts from 1, ends at N. Each inciments by 1
    """
    f = open(invoice_set, 'r')
    N_k = f.readline()      # get N, k fron first line
    N_k = N_k.split()
    N = int(N_k[0])
    k = int(N_k[1])
    
    invoices = [0]*N   # an array to contain all invoices
    # Python uses list, but we're simply demonstrating algorithm
    for line in f:
        inv = int(line)     # invoice number
        invoices[inv-1] = 1     # array starts at 0, but inv starts at 1. Assume this takes O(1)
        
    f = open('invoice_miss.txt','w')
    for i in range(len(invoices)):
        if invoices[i] == 0:
            f.write(str(i+1)+'\n')  # Shifted i down before, now shift up
        
    f.close()

    
find_miss_inv_pp("testdata.txt")
