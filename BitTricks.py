'''
    BIT MANIPULATION TRICKS :-
   --------------------------
   
1) DIVIDING BY 2 AND MULTIPLYING BY 2 :-
   ------------------------------------
   -> To divide number by 2 for 'i' times, just do right shift.
   Ex:- n = 10                                 Process
        i = 2                                ------------
        print(n >> i)   #2                    10 >> 2 => divide 10 by 2 for 2 times => 10//2 = 5 => 5//2 = 2

   -> To multiply number with 2 for 'i' times, just do left shift.
   Ex:- n = 10                                 Process
        i = 2                                ------------
        print(n << i)                         10 << 2 => multiply 10 with 2 for 2 times => 10*2 = 20 => 20*2 = 40

  Formulae:-  RIGHT SHIFT =  N // (2**i)
              LEFT SHIFT  =  N * (2**i)

2) CHECK WHETHER THE GIVEN NUMBER IS EVEN OR ODD USING SHIFTING OPERATORS :-
   ------------------------------------------------------------------------

   For odd numbers, the LSB bit is always a SET BIT. So, do binary AND with 1 to check odd (or) even.
   CODE :
   ------
   n = 10
   if( n & 1 ):
       print("ODD")
   else:
       print("EVEN")

3) CONVERT UPPERCASE TO LOWERCASE and VICE VERSA :-
   ------------------------------------------------
   We should observe a pattern that is hidden in the binary formats of upper and lowercase letters.

   Ex:- A : 0 0 0 0 1 0 0 0 0 0 1            B : 0 0 0 0 1 0 0 0 0 1 0
        a : 0 0 0 0 1 1 0 0 0 0 1            b : 0 0 0 0 1 1 0 0 0 1 0

    Observe..!! The 5th bit is a SET BIT in lowercase letters, where it is UNSET BIT in uppercase letters and the rest are as it is.

    CODE :-
    ------
    UPPER TO LOWER                           LOWER TO UPPER

    A = 'A'                                  a = 'a'
    a = chr(ord(A) | (1<<5))                 A = chr(ord(a) & (~(1 << 5)))
    print(a)                                 print(A)

    The code for UPPER TO LOWER works... where as the code for LOWER TO UPPER doesn't work. It is because, the value of ~(1<<5) goes out of bound (not i in range of 0 to 255).
    So, to avoid this, we just take a binary number where the 5th bit is unset i.e., 00001011111 (which is the ascii of underscore ).
    Do binary AND whith the given character.

    print(chr(ord('a')&ord('_')))    #LOWERCASE TO UPPERCASE
    print(chr(ord('A')|ord(' ')))    #UPPERCASE TO LOWERCASE  (1<<5) is the ascii value of space(' ')

4) CHECK WHETHER GIVEN NUMBER IS POWER OF 2 OR NOT :-
   --------------------------------------------------
   CODE:
   ----
   n = 8                                                             1 0 0 0  => 8  (n)
   if(n & (n-1)):                                           (AND)    0 1 1 1  => 7  (n-1)
       print("NOT POWER OF 2")                                   ---------------------------
   else:                                                             0 0 0 0  => 0
       print("POWER OF 2")                                       ---------------------------

5) COUNTING THE NUMBER OF SET BITS IN GIVEN NUMBER :-
   --------------------------------------------------
   APPROACH - 1                                         APPROACH - 2
   --------------                                      ----------------
   def countSetBits(n):                                def countSetBits(n):
       cnt = 0                                            cnt = 0
       while(n != 0):                                     while n>0:
           if((n&1) == 1):                                    n = n&(n-1)
               cnt += 1                                       cnt += 1
           n >>= 1                                        return cnt
        return cnt                                     print(countSetBits(10))   #2
    print(countSetBits(10))   #2

'''

    

    
