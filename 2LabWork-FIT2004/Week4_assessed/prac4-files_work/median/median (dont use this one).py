from heapq import heappush, heappop
"""
Library heapq starts from 0: children are 2*k+1, 2*k+2 instead.
Root of heap is at index 0.
"""


def median_heap(num_file):
    num_in = open(num_file,'r')
    num_out = open('testtestdata_out.txt','w')
    heap1 = []  # insert to heap1 first
    heap2 = []  
    
    for i in num_in:
        num = int(i)
        if len(heap1) == 0:
            heap1.append(num)
            median = num
        elif len(heap2) == 0:    # need to make two heaps first before making comparison
            heap2.append(num)
            median = int((heap1[0]+heap2[0])/2)
            if heap1[0] >= heap2[0]:
                # if 1st element is larger than 2nd, heap1 is a minheap 
                # (contains 2nd greater half of all numbers with least num at top)
                heapmin = heap1 # need to make new var so we can separate it in else:
                heapmax = heap2
            else:
                # otherwise, heap1 is a maxheap.
                # (contains 1st lower half of all numbers with biggest num at top)
                heapmax = heap1
                heapmin = heap2
            heapmax[0] *= -1    # heappush uses minheap. Need to apply -1 to reverse order
        else:   # if both are not empty
            print(heapmax, heapmin) ###
            l_max = len(heapmax)
            l_min = len(heapmin)
            
            # Determine Heap for num to get into
            if num >= median:   # belong to larger numbers
                if l_min - l_max >= 1:    # >= 1 elem in heapmin to heapmax (should be 1 only)
                    heappush(heapmax, (-1)*heappop(heapmin)) # least great to best lesser
                    # So the roots are always the elements in the middle
                    l_max += 1      ### WHAT SHOULD WE PUT HERE??
                heappush(heapmin, num)  
            else:               # belong to smaller numbers
                if l_max - l_min >= 1:
                    heappush(heapmin, (-1)*heappop(heapmax))
                    l_min += 1      ### WHAT SHOULD WE PUT HERE?? 
                heappush(heapmax, num*(-1))
                
            # Determine median
            if l_min - l_max == 1:    # len() takes O(1)
                median = heapmin[0]
            elif l_max - l_min == 1:
                median = heapmax[0]*(-1)    # convert back
            elif l_max == l_min:
                median = (heapmin[0]+heapmax[0]*(-1))//2
            print(heapmax, heapmin)   ###
            
        num_out.write(str(median)+'\n')
        print(median)   ###
        
    num_in.close()
    num_out.close()
    
median_heap("testdata.txt")
                
            
