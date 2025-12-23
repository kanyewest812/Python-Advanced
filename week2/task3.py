v = input()
a = v[0]
op = v[1]
b = v[2]
c = v[4]

if a == 'x':
    if op == '+':
        x = int(c) - int(b)
    else:
        x = int(c) + int(b)

elif b == 'x':
    if op == '+':
        x = int(c) - int(a)
    else:
        x = int(a) - int(c)

else:
    if op == '+':
        x = int(a) + int(b)
    else:
        x = int(a) - int(b)

print(x)
