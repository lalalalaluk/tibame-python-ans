n = int(input())

max_prime = 2

# for i in range(2, n+1):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#     if is_prime:
#         max_prime = i

# print(max_prime)

index = 2
while index <= n:
    is_prime = True
    j = 2
    while j < index:
        if index % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        max_prime = index
        
    index += 1
print(max_prime)

