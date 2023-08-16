# A=10 B=11 C=12 D=13 E=14 F=15 G=16 H=17 I=34 J=18 K=19 L=20
# M=21 N=22 O=35 P=23 Q=24 R=25 S=26 T=27 U=28 V=29 W=32 X=30
# Y=31 Z=33

identity = input()

checksum = 0

if identity[0] == 'A':
    checksum = 1 + 0 * 9
elif identity[0] == 'B':
    checksum = 1 + 1 * 9
elif identity[0] == 'C':
    checksum = 1 + 2 * 9
elif identity[0] == 'D':
    checksum = 1 + 3 * 9
elif identity[0] == 'E':
    checksum = 1 + 4 * 9
elif identity[0] == 'F':
    checksum = 1 + 5 * 9
elif identity[0] == 'G':
    checksum = 1 + 6 * 9
elif identity[0] == 'H':
    checksum = 1 + 7 * 9
elif identity[0] == 'I':
    checksum = 1 + 8 * 9
elif identity[0] == 'J':
    checksum = 1 + 9 * 9
elif identity[0] == 'K':
    checksum = 2 + 0 * 9
elif identity[0] == 'L':
    checksum = 2 + 1 * 9
elif identity[0] == 'M':
    checksum = 2 + 2 * 9
elif identity[0] == 'N':
    checksum = 2 + 3 * 9
elif identity[0] == 'O':
    checksum = 2 + 4 * 9
elif identity[0] == 'P':
    checksum = 2 + 5 * 9
elif identity[0] == 'Q':
    checksum = 2 + 6 * 9
elif identity[0] == 'R':
    checksum = 1 + 1 * 9
elif identity[0] == 'S':
    checksum = 1 + 1 * 9
elif identity[0] == 'T':
    checksum += 2 + 7 * 9
elif identity[0] == 'U':
    checksum += 2 + 8 * 9
elif identity[0] == 'V':
    checksum += 2 + 9 * 9
elif identity[0] == 'W':
    checksum += 3 + 2 * 9
elif identity[0] == 'X':
    checksum += 3 + 0 * 9
elif identity[0] == 'Y':
    checksum += 3 + 1 * 9
else:
    checksum += 3 + 3 * 9

checksum += int(identity[1]) * 8
checksum += int(identity[2]) * 7
checksum += int(identity[3]) * 6
checksum += int(identity[4]) * 5
checksum += int(identity[5]) * 4
checksum += int(identity[6]) * 3
checksum += int(identity[7]) * 2
checksum += int(identity[8])
checksum += int(identity[9])

if checksum % 10 == 0:
    print('合法')
else:
    print('不合法')