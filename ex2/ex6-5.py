
while True:
    try:
        n = int(input())
        score = 0
        if n <= 10:
            score = n * 6
        elif n <= 20:
            score = 60 + (n - 10) * 2
        elif n <= 40:
            score = 80 + (n - 20) * 1
        print(score)
    except:
        break
