m1,m2,m3=0,0,0
for i in range(0,int(input())):
  a = int(input())
  if a % 3 == 0:
    m1+=1
  elif a % 3 == 1:
    m2+=1
  else:
    m3+=1
print(m1,m2,m3)
