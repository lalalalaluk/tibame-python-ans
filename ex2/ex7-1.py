index=0
while 1:
  a=int(input())
  if a == 0:
    break
  box=list(map(int,input().split()))
  total=sum(box)/a
  ans=0
  
  for i in box:
    if i > total:
      ans+=i-total
  index+=1
  print(f"Set #{index}\nThe minimum number of moves is {int(ans)}.\n")