items = input().split()

freq = {}

for x in items:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("Purchase frequency:")
for x in freq:
    print(f"{x}: {freq[x]}")

maxitem = ""
maxcount = 0

for x in freq:
    if freq[x] > maxcount:
        maxcount = freq[x]
        maxitem = x

print("Most popular item:", maxitem)

once = []
for x in freq:
    if freq[x] == 1:
        once.append(x)

print("Purchased once:", " ".join(once))

order = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Sorted by frequency:")
for x, cnt in order:
    print(x, cnt)