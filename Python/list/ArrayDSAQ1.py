""" Problem statement
You are given an array/list consisting of 0 and 1 only. Your task is to find the sum of the number of subarrays that contains only 1 and the number of subarrays that contains only 0.

An array 'C' is a subarray of array 'D' if 'C' can be obtained from 'D' by deletion of several elements from the beginning and several elements from the end. Example :

Let 'ARR' = [1,0,0] then the possible subarrays of 'ARR' will be: {1}, {0}, {0}, {1,0}, {0,0}, {1,0,0}.
Example
If the given array 'ARR' = [1,0,0,0,1,1,0,1]
Then the number of 1’s subarrays will be 5. [{1},{1},{1},{1,1},{1}]
And the number of 0’s subarrays will be 7. [{0},{0},{0},{0,0},{0,0},{0,0,0},{0}]
So our answer will be 5 + 7 = 12.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:-
1 <= T <= 100
1 <= N <= 5000
0 <= ARR[i] <= 1

Where ARR[i] denotes the elements of the array."""

#note
"""Important: The subarray must be contiguous (continuous elements). """
#note
"""👉 Formula:
For a block of length k, the number of subarrays k*(k+1)/2 ​

Example:

If block = [1,1] (length k=2)
Subarrays = 2×3 / 2 = 3 → {1}, {1}, {1,1}

If block = [0,0,0] (length k=3)
Subarrays = 3×4 / 2 = 6 → {0}, {0}, {0}, {0,0}, {0,0}, {0,0,0} """





from os import *
from sys import *
from collections import *
from math import *

def numberofSubarrays(arr, n):
   total=0
   i=0
   while i<n:
       j=i
       
       while j<n and arr[j]==arr[i]:
           j+=1
       length=j-i
       total+=(length*(length+1))//2
       i=j
   return total
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    arr=list(map(int,input().strip()))
    print(numberofSubarrays(arr,n))





    
