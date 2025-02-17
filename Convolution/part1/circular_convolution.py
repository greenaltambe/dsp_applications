L = int(input("Enter the length of x[n] i.e. L = "))
x = [float(input("Enter the value of x[n] : ")) for i in range(L)]

M = int(input("Enter the length of y[n] i.e. M = "))
h = [float(input("Enter the value of y[n] : ")) for i in range(M)]

N = max(L, M)
x += [0] * (N - L)
h += [0] * (N - M)

_h = [h[0]] + h[1:][::-1]
print(h)

matrix = []
for i in range(N):
  matrix.append(_h[-i:] + _h[:-i]);

y = [0] * N

for i in range(N):
  for j in range(N):
    y[i] += x[j] * matrix[i][j]

print("\nx[n] = ", end = " ")
for i in range(N):
  print(x[i], end = "  ")

print("\n\nh[n] = ", end = " ")
for i in range(N):
  print(h[i], end = "  ")

print("\n\ny[n] = ", end = " ")
for i in range(N):
  print(y[i], end = "  ")