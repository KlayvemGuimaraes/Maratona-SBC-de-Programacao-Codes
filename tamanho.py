# -- coding: utf-8 --

num = input()

while len(num) >= 1:
  print(num)
  if len(num) != 1:
    num = str((int(num[0:len(num) - 1]) * 3) + int(num[-1]))
  else:
    break
