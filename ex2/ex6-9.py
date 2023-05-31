
number = input()
elements = input().split()

all = list(map(int, input().split()))

set_all = set(all)


print(len(set_all))
for i in sorted(list(set_all)):
    print(i, end=' ')

