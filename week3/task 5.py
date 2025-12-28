def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

alym = A * D - B * C
bolym = B * D

g = gcd(abs(alym), bolym)

alym //= g
bolym //= g

print("Result:", alym, "/", bolym)


#task 5.2
n = int(input("Enter a number: "))

print("Divisors:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
