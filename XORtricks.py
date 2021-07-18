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


'''
    SWAPPING 2 NUMBERS
---------------------------

a = a^b                       
b = b^a                     =>   b = b^(a^b) =>  b = b^b^a  => b = a
a = a^b                     =>   a = (a^b)^a =>  a = a^a^b  => a = b

XOR of same numbers is always results in 0. [ a^a = 0 ]
XOR of any number with 0 is always results in that number. [ x^0 = x ]

'''

a,b = map(int,input().split())
print("Values before swapping : ",a,b)
a = a^b
b = b^a
a = a^b
print("Values after swapping : ",a,b)
