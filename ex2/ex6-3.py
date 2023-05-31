
while True:
    try:
        n = list(map(int, input().split()))

        total = int(n[0])

        if sum(n[1:]) / len(n[1:]) >= 59:
            print('no')
        else:
            print('yes')
    except:
        break


