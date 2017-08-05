from sys import stdin
import math
import sys
import random



N = int(stdin.readline())


f = open('testdata.txt', 'w')

random.seed(int(N))


for num in range(N):
   val = random.randint(1,10000)
   s = str(val) + '\n'
   f.write(s)
   
f.close()   
      
