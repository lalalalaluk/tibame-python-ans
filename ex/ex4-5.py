n = int(input())

times = 0

while n > 0:
    if n % 2 == 1:
        n -= 1
    elif n % 2 == 0:
        n /= 2
    times += 1

print(times)