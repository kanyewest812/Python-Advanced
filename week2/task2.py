a = input()
b = input()

с = len(b)
count = 0

for i in range(len(a) - с + 1):
    part = a[i:i+с]
    if part in (b + b):
        count += 1

print(count)
