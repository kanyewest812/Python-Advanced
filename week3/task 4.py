def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))

alym = A * D
bolym = B * C

g = gcd(alym, bolym)

alym //= g
bolym //= g

print("Result of division:", alym, "/", bolym)


#task 4.2
def cinside(x, y, a, b, r):
    return (x - a) ** 2 + (y - b) ** 2 < r ** 2


a = float(input("Center x: "))
b = float(input("Center y: "))
r = float(input("Radius: "))

count = 0

for i in range(3):
    x = float(input("Point x: "))
    y = float(input("Point y: "))
    if cinside(x, y, a, b, r):
        count += 1

print("Points inside:", count)
