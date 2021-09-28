import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a == 0 or b == 0 or c == 0:
  print('ezen egyenlet megoldásánál nem használható a megoldóképlet')
else:
  # diszkrimináns
  d = math.pow(b, 2) + 4 * a * c
  if d < 0: 
    print('valós számok halmazán nincw megoldása az egyenletnek')
  elif d == 0:
    print(f'x = {- b / (2 * a)}')
  else:
    print(f'x1 = {- b + math.sqrt(d) / (2 * a)}')
    print(f'x2 = {- b - math.sqrt(d) / (2 * a)}')

print('ennyi kthxbye')