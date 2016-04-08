import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
total = 0
for x in xrange(n):
 total += arr[x]
print total
