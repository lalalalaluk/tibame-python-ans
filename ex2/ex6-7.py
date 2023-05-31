
t = int(input())

for i in range(t):
    a = int(input())
    b = int(input())
    odd_sum = 0
    for j in range(a, b + 1):
        if j % 2 == 1:
            odd_sum += j
    print("Case " + str(i + 1) + ": " + str(odd_sum))
