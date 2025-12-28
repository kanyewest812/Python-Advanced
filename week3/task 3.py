import math

def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)


a1 = float(input("First leg of triangle 1: "))
b1 = float(input("Second leg of triangle 1: "))

a2 = float(input("First leg of triangle 2: "))
b2 = float(input("Second leg of triangle 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse of triangle 1:", h1)
print("Hypotenuse of triangle 2:", h2)

if h1 > h2:
    print("Hypotenuse of triangle 1 is greater")
elif h1 < h2:
    print("Hypotenuse of triangle 2 is greater")
else:
    print("Both hypotenuses are equal")


#task 3.2
text = input("Enter a string: ")

words = text.split()
result = []

for word in words:
    sorti = "".join(sorted(word))
    result.append(sorti)

print("Result:", " ".join(result))
