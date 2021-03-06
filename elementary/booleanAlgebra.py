'''
In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in which the values of the variables are true or false, 
typically denoted with 1 or 0 respectively. 
Instead of elementary algebra where the values of the variables are numbers and the main operations are addition and multiplication, 
the main operations of Boolean algebra are the conjunction (denoted and), the disjunction (denoted or (v)) and the negation (denoted not).

In this mission you should implement some boolean operations:
- "conjunction" denoted x and y, satisfies x and y = 1 if x = y = 1, x and y = 0 otherwise.
- "disjunction" denoted x or y, satisfies x or y = 0 if x = y = 0, x or y = 1 otherwise.
- "implication" (material implication) denoted x -> y and can be described as "not x or y". 
  If x is true then the value of x -> y is taken to be that of y. But if x is false then the value of y can be ignored; 
  however the operation must return some truth value and there are only two choices, 
  so the return value is the one that entails less, namely true.
- "exclusive" (exclusive or) denoted x xor y and can be described as (x or y) and not (x and y). 
  It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
- "equivalence" denoted x == y and can be described as not (x xor y). It's true just when x and y have the same value.

Here you can see the truth table for these operations:

 x | y | x and y | x or y | x -> y | x xor y | x == y |
-------------------------------------------------------
 0 | 0 |    0    |   0    |    1   |    0    |    1   |
 1 | 0 |    0    |   1    |    0   |    1    |    0   |
 0 | 1 |    0    |   1    |    1   |    1    |    0   |
 1 | 1 |    1    |   1    |    1   |    0    |    1   |
-------------------------------------------------------
You are given two boolean values x and y as 1 or 0 and you are given an operation name as described earlier. You should calculate the value and return it as 1 or 0.

Input: Three arguments. X and Y as 0 or 1. An operation name as a string.
Output: The result as 1 or 0.

How it is used: Here you will learn how to work with boolean values and operators. You even get to think about numbers as booleans.

Precondition: x in (0, 1), y in (0, 1), operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
'''

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction": return int(x and y)
    elif operation == "disjunction": return int(x or y)
    elif operation == "implication": return int((not x) or y)
    elif operation == "exclusive": return int(x != y)
    elif operation == "equivalence": return int(x == y)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 0, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(1, 1, "exclusive") == 0, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
