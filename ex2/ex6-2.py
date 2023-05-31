


while 1:
    n = int(input())
    if n == 0:
        break

    result = []
    for i in range(1, n):
        if i % 7 == 0:
            continue
        result.append(str(i))
    
    print(" ".join(result))


