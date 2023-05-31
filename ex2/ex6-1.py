a = int(input())


t = 0
tone = 0
ttwo = 0

while a >= 1:
    if a % 3 == 0:
        t+=1
    elif a % 3 == 1:
        tone +=1 
    elif a % 3 == 2:
        ttwo +=1
    a -= 1
print(str(t)+" "+str(tone)+" "+str(ttwo))
