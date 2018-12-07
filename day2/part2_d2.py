from collections import Counter
import sys

def diff(s1, s2):
    A = [i for i in xrange(len(s1)) if s1[i] != s2[i]]
    count = len(A)
    return count, A

List_letters = []
count = 0

with open("input.txt") as f:
#width open(sys.argv[1]) as f:
    for line in f:
        List_letters.append(line.strip())

L = len(List_letters)
for i in xrange(0, L-1):
    for j in xrange(i+1,L):
        count,A = diff(List_letters[i], List_letters[j])
        if count == 1:
            h = List_letters[i]
            print h[:A[0]]+h[(A[0]+1):]
