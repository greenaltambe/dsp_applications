L = int(input("Enter the length of x[n] i.e. L = "))
x = []
for i in range(L):
  x.append(float(input("Enter the value of x[n] : ")))

M = int(input("Enter the length of y[n] i.e. M = "))
h = []
for i in range(M):
  h.append(float(input("Enter the value of h[n] : ")))

y = []

N = L + M - 1

for i in range(N):
  y.append(0)

for i in range(L):
  for j in range(M):
    y[i+j] += x[i] * h[j]

print("\nx[n] = ", end = " ")
for i in range(L):
  print(x[i], end = "  ")

print("\n\nh[n] = ", end = " ")
for i in range(M):
  print(h[i], end = "  ")

print("\n\ny[n] = ", end = " ")
for i in range(N):
  print(y[i], end = "  ")