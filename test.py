input = input().split(sep="-")
r = int(input[0])
b = int(input[1])
b1 = 4
r1 = 1

if r == 3 and b == 0:
    print("win")
elif b+b1 > r+r1:
    print('lost')
elif b+b1 == r+r1:
    print('penalty')
else:
    print("win")
