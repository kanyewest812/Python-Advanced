import math

def triangle(a):
    return (math.sqrt(3) / 4) * a * a

a = float(input("Side of the hexagon: "))
hexagon = 6 * triangle(a)
print("Regular hexagon area:", hexagon)

#task 2.2
for i in range(3):
    x = float(input("First side of rectangle: "))
    y = float(input("Second side of rectangle: "))
    area = x * y
    print("Rectangle area:", area)
