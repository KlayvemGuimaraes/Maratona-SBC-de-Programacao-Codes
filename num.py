# -- coding: utf-8 --

n, k = map(int, input().split())
a = 0

for i in range(1, 2 * n + 1):
  if (i * i - k) % (2 * n + 1) == 0 and i * i != k:
    a = (i * i)
print(a)