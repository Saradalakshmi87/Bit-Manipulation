# Bit-Manipulation

'''
Working on bytes, or data types comprising of bytes like ints, floats, doubles or even data structures which stores large amount of bytes is normal for a programmer.

In some cases, a programmer needs to go beyond this - that is to say that in a deeper level where the importance of bits is realized.

Operations with bits are used in Data compression (data is compressed by converting it from one representation to another, to reduce the space),Exclusive-Or Encryption
(an algorithm to encrypt the data for safety issues).

In order to encode, decode or compress files we have to extract the data at bit level. Bitwise Operations are faster and closer to the system and sometimes optimize the program
to a good level.

    BITWISE OPERATORS
------------------------------

1) Bitwise AND :-       
   -----------
   If both bits in the compared position of the bit patterns are 1, the bit in the resulting bit pattern is 1, otherwise 0.
   Ex:- A = 5, B = 3
     
   Binary Representations of A and B are 101 and 011                                                   

          1  0  1   => 5
        &
          0  1  1   => 3
        -----------
          0  0  1   => 1
        -----------

2) Bitwise OR:- 
   ----------
   If both bits in the compared position of the bit patterns are 0, the bit in the resulting bit pattern is 0, otherwise 1.
   Ex:- A = 5, B = 3

   Binary Representations of A and B are 101 and 011

          1  0  1   =>5
        |
          0  1  1   => 3
        -----------
          1  1  1   => 7
        -----------
3) Bitwise XOR:-
   -----------
   If both bits in the compared position of the bit patterns are 0 or 1, the bit in the resulting bit pattern is 0, otherwise 1.
   Ex:- A = 5, B = 3

   Binary Representations of A and B are 101 and 011

          1  0  1    => 5
        ^
          0  1  1    => 3
        -----------
          1  1  0    => 6
        -----------

4) Bitwise NOT:- 
   -----------
   if the ith bit is 0, it will change it to 1 and vice versa. Bitwise NOT is nothing but simply the one’s complement of a number.
   Ex:- A = 5 (Binary is, 101)  =>   ~A = 010 (decimal is, 2)

5) Bitwise Left shift:-  
   -------------------   
   Left shift operator is a binary operator which shift the some number of bits, in the given bit pattern, to the left and append 0 at the end.
   Left shift is equivalent to multiplying the bit pattern with  2 to the power k (2^k, if we are shifting k bits ).

6) Bitwise Right shift:-  
   --------------------   
   Right shift operator is a binary operator which shift the some number of bits, in the given bit pattern, to the right and append 1 at the end.
   Right shift is equivalent to dividing the bit pattern with 2//k ( if we are shifting k bits ).

NOTE :- Bitwise AND, OR and XOR takes equal length bit patterns.

    BASIC KNOWLEDGE
--------------------------

  i) a & 0  = 0                     i)  a | 0  = a                     i) a ^ 0  = a

 ii) a & a  = a                     ii) a | a  = a                    ii) a ^ a   = 0
           
           / 1 , if odd                       / a , if odd                      / (a - 1) , if odd
iii) a & 1                         iii) a | 1                        iii) a ^ 1 
           \ 0 , if even                      \ (a + 1) , if even               \ (a + 1) , if even
           


'''

