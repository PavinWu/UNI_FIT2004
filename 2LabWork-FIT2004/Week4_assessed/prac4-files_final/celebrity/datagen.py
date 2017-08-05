from sys import stdin
import math
import sys
import random



N = int(stdin.readline())
k = int(stdin.readline())

f = open('testdata.txt', 'w')

random.seed(int(N))


s = str(N) + ' ' + str(k) + '\n'
f.write(s)
for num in range(N):
   val = random.randint(1,10000000)
   s = str(val) + '\n'
   f.write(s)
   if num%1000000 == 0 and num > 0:
       print(num)
   
f.close()   
      
