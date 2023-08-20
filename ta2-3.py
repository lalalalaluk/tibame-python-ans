n = int(input())

if n == 1:
    print('0')
elif n == 2:
    print('1')
else:
    first = 0
    second = 1

    # for i in range(2, n):
    #     first, second = second, first + second

    # print(second)

    index = 2
    while index < n:
        first, second = second, first + second
        index += 1
    print(second)

    for i in range(2, n):
        temp = first + second
        first = second
        second = temp

    print(second)
