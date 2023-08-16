a = input().split()
if a[0] == '星期六' or a[0] == '星期日':
    print('不開市')
else:
    print(int(a[1])*int(a[2]))
