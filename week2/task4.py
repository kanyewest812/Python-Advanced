n, m = map(int, input().split())
lenst = input()

lenwords = set()

for i in range(n - m + 1):
    word = lenst[i:i+m]
    lenwords.add(word)

print(len(lenwords))