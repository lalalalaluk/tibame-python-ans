in_txt = input().split()


# i = 0
# ans = ''
# while i < len(in_txt):
#     ans += str(int(in_txt[i]) +1) + ' '
#     i += 1

# print(ans)

# def my_func(x):
#     return int(x) + 1

# numbers = list(map(my_func, in_txt))
# print(numbers)

# for迴圈
for i in range(len(in_txt)):
   in_txt[i] = str(int(in_txt[i]) + 1)

print(" ".join(in_txt))