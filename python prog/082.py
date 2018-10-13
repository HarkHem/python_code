import sys
import math
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'a')
import itertools
s = []
N = input()
A = list(itertools.permutations(range(2,N+1)))
for row in A:
    s.append(1)
    s.extend(row)
    print(' '.join([str(elem) for elem in s]))
    del s [:]

sys.stdout.close()
