def triangle(a, b):
    return a * b / 2


def rectangle(a, b):
    return a * b


x = float(input("Enter side X: "))
y = float(input("Enter side Y: "))
z = float(input("Enter side Z: "))
t = float(input("Enter side T: "))

area = triangle(x, y) + rectangle(z, t)
print("Quadrilateral area:", area)


#task 7.2
n = int(input("Non-negative integer: "))

octal = format(n, 'o')
octal_10 = octal.zfill(10)

print("10-digit octal code:", octal_10)
