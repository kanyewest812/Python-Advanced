print("Еhe desired figure:")
print("1 - Circle")
print("2 - Rectangle")
print("3 - Triangle")

choice = int(input("which one?: "))

if choice == 1:
    r = float(input("Radius: "))
    area = 3.14 * r * r
    print("Circle area:", area)

elif choice == 2:
    a = float(input("Length: "))
    b = float(input("Width: "))
    area = a * b
    print("Rectangle area:", area)

elif choice == 3:
    b = float(input("Base: "))
    h = float(input("Height: "))
    area = 0.5 * b * h
    print("Triangle area:", area)

else:
    print("Invalid choice")

#task 1.2
for i in range(3):
    num = list(map(int, input("Enter numbers: ").split()))

    ovrall = sum(num)
    arif = ovrall / len(num)

    print("Sum:", ovrall)
    print("Arithmetic mean:", arif)