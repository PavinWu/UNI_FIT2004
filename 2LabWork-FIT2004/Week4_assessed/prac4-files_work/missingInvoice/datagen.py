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
array = [x+1 for x in range(N)]

for i in range(k):
   val = random.randint(0,N-1)
   while array[val] < 0:
      val = random.randint(0,N-1)
   array[val] *=  -1
   

random.shuffle(array)

for i in range(N):
   if array[i] > 0:
      s = str(array[i]) + '\n'
      f.write(s)
   
f.close()   
      
