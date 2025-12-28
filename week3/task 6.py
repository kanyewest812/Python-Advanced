import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


Ann = int(input("A: "))
Bnn = int(input("B: "))

g = gcd(Ann, Bnn)
l = (Ann * Bnn) // g

print("GCD:", g)
print("LCM:", l)


#task 6.2
def triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))
e = float(input("Enter diagonal: "))

area1 = triangle(a, b, e)
area2 = triangle(c, d, e)

print("Quadrilateral area:", area1 + area2)
