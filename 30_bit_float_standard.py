#30-bit float standard
#Note this standard treats the original bit sequence as if it were a Python3 array of integers. Also, this is written as Python3 code, but with only \n treated as the newline character and only \t treated as the one and only one method by which an indentation happens (when \t is converted to the tab character in the Python3 interpreter).\n
# let r: list=[bit for bit in thirty_bit_float_sequence_that_has_most_significant_bit_at_position_0]\n

result: float=1\n
exist1: int=0\n
if r[0]==1:\n
    \tresult*=-1\n
    \texist1=1\n
ex: int=0\n
for j in range(1, 10):\n
    \tex=2*ex+r[j]\n
if ex>0:\n
    \texist1=1\n
ex-=256\n
frac: int=0\n
for j in range(10, 30):\n
    \tfrac=2*frac+r[j]\n
if frac>0:\n
    \texist1=1\n
result=result*((frac/1048576.0+exist1)**ex)\n
return result\n
