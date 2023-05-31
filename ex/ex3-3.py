year = int(input())

if year % 4 != 0:
  print('a normal year')
if year % 4 == 0 and year % 100 != 0:
  print('a leap year')
if year % 100 == 0 and year % 400 != 0:
  print('a normal year')
if year % 400 == 0:
  print('a leap year')