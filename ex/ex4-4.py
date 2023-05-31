step = list(input())

LF = 0
UD = 0

# for s in step:
#     if s == 'L':
#         LF -= 1
#     elif s == 'R':
#         LF += 1
#     elif s == 'U':
#         UD += 1
#     elif s == 'D':
#         UD -= 1

index = 0
while index < len(step):
    if step[index] == 'L':
        LF -= 1
    elif step[index] == 'R':
        LF += 1
    elif step[index] == 'U':
        UD += 1
    elif step[index] == 'D':
        UD -= 1   
    index += 1

if LF == 0 and UD == 0:
    print('Y')
else:
    print('N')