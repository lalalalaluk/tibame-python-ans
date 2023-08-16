n = int(input())
sum = 0
# for i in range(n):
#     sum += i + 1
# print(sum)

index = 1
while index <= n:
    sum += index
    index += 1

print(sum)