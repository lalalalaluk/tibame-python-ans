x, y = input().split()
x = int(x)
y = int(y)

# i = 1
# while i <= x:
#     j = 1
#     while j <= y:
#         print(f'{i}X{j}={j*i}')
#         j += 1
#     i += 1

# i = 1
# while i <= x:
#     j = 1
#     while j <= y:
#         print(f'{i}X{j}={j*i}')
#         j += 1 
#     i += 1


for i in range(1, x+1):
    j = 1
    for j in range(1, y+1):
        print(f'{i}X{j}={j*i}')
        j += 1
    i += 1