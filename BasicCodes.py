'''

    BIT MANIPULATION TRICKS
----------------------------------

1) Decimal to Binary :-
   -------------------
   Let the deciaml number be N,

   N = 9
   for i in range(8,-1,-1):
       print(((N >> i) & 1),end = '')

   The above code results in 000001001

2) CHECK WHETHER ith BIT IS SET OR NOT :-
   -------------------------------------
   To check whether ith bit is set or not, we take a number in such a way that, where only ith bit is set and the rest are zeores.

   Ex:-  let N = 5 (101). Check whether 1st bit is set or not ?

   So, take a number where only 1st bit is set i.e, 010.
   Now, do binary AND.
   If the result is zero, then it's an unset bit. Otherwise, the ith bit in the given number is a set bit.

      1  0  1
    &
      0  1  0
    -----------
      0  0  0
    -----------

    Now, the point is, how to obtain that number??

    It is simple!! Just do (1 << i)

    CODE
    ----

    n = 9
    i = 0
    if((n & (1 << i))!=0):
        print("SET BIT")
    else:
        print("NOT SET BIT")

3) SETTING ith BIT:-
   ----------------
    CODE
    ----
    Ex:- Let N = 9. Set the 1st bit in N
    
    a = 9                                                                 0 0 0 0 0 0 0 1 0 0 1  => 9
    i = 1                                                           (OR)  0 0 0 0 0 0 0 0 0 1 0  => 2 (where 1st bit is set)
    print(bin(a | (1<<i)))                                              ---------------------------------
                                                                          0 0 0 0 0 0 0 1 0 1 1  => 11
                                                                        ---------------------------------

4) UNSETTING ith BIT :-
   --------------------
   For this, we should take a number in such a way that, where ith bit is unset and the rest all are set.

   Ex:- let N = 9 and i = 3                                              0 0 0 0 0 0 0 1 0 0 1  => 9
                                                                  (AND)  1 1 1 1 1 1 1 0 1 1 1
                                                                       -------------------------------
                                                                         0 0 0 0 0 0 0 0 0 0 1  => 1
                                                                       -------------------------------
  Now, how to obtain the number ( 1 1 1 1 1 1 1 0 1 1 1 ). This number is actually inversion ( 0 0 0 0 0 0 0 1 0 0 1 ) of the number, where ith bit is set and remaining are unset.

  ~(00000001001) => (11111110111)

  CODE
  ----
  a = 9
  i = 3
  print(bin(a & ~(1 << i)))

5) TOGGLING BITS :-
   ----------------
   Let N be the given number. Toggle ith bit (i.e, if the bit is 0, toggle it to 1 and if bit is 1, toggle it to 0).

   CODE
   ----
   N = 9                                                                  0 0 0 0 0 0 0 1 0 0 1  => 9
   i = 2                                                            (XOR) 0 0 0 0 0 0 0 0 1 0 0  => (1<<2)
   print(bin(a ^ (1 << i)))                                              --------------------------
                                                                          0 0 0 0 0 0 0 1 1 0 1  => 13
                                                                         --------------------------
'''
