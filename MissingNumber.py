'''
    QUESTIONS ON XOR
-------------------------

Given an array A of n integers. All integers are present in even count except one. Find that one integer which has odd count in O(n) time and O(1) space.

i/p format :-
..........

9
4 2 1 1 4 2 5 1 1

o/p format :-
..........

5

'''

n = int(input())
l = [int(i) for i in input().split()]
ans = 0
for i in range(len(l)):
    ans ^= l[i]
print(ans)
