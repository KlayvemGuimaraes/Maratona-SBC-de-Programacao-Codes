# -- coding: utf-8 --

linha = input()
estranho = 0
alice = 0

for i in range(0, 3):
  if linha[i] != 'O' and linha[i] != 'X':
    estranho = 1

  if linha[i] == 'X':
    alice += 1

if alice != 2 or estranho > 0:
  print('?')

else:
  if linha[1] == 'O' and linha[2] == 'X':
    print('*')
  else:
    print('Alice')
