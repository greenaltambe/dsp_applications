import numpy as np

L = int(input("Enter the length of x[n] i.e. L = "))
x = [float(input("Enter the value of x[n] : ")) for i in range(L)]

M = int(input("Enter the length of y[n] i.e. M = "))
h = [float(input("Enter the value of y[n] : ")) for i in range(M)]

y = np.correlate(x, h, mode='full')
print("y[n] =", y)
