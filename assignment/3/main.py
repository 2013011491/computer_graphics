import numpy as np
import math

M=np.arange(2,27)
print(M)
print("\n")
a=M.reshape(5,5)
print(a)
print("\n")
a[1:4,1:4]=0
print(a)
print("\n")
a=a@a
print(a)
print("\n")
v=a[0,]
print(math.sqrt(v@v))
