line = input()
a, b = line.split()
a = int(a)
b = int(b)

if a <= b:
    print(a, b)
elif b <= a:
    print(b,a)
