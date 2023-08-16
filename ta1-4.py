

in_txt = input()

in_list = in_txt.split(',')

my_list = in_list[0].split()
com_list = in_list[1].split()

# print(my_list)
# print(com_list)

count = 0

if my_list[0] in com_list:
    count += 1

if my_list[1] in com_list:
    count += 1

if my_list[2] in com_list:
    count += 1

if my_list[3] in com_list:
    count += 1

if my_list[4] in com_list:
    count += 1

if count < 3:
    print(0)
elif count == 3:
    print(100)
elif count == 4:
    print(1000)
else:
    print(10000)