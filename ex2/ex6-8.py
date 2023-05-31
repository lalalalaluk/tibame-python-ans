
t = int(input())

for i in range(t):
    n = input().split()

    n1 = int(n[0])
    n2 = int(n[1])
    n3 = int(n[2])

    if n1 == 1:
        print(n2+n3)
    elif n1 == 2:
        print(n2-n3)
    elif n1 == 3:
        print(n2*n3)
    elif n1 == 4:
        print(int(n2/n3))

