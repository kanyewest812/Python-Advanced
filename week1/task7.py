first = float(input("First number: "))
op = input("Operation (+, -, *, /): ").strip()
second = float(input("Second number: "))

if op == "+":
    result = first + second
elif op == "-":
    result = first - second
elif op == "*":
    result = first * second
elif op == "/":
    result = "Error: division by zero!" if second == 0 else first / second
else:
    result = "Unknown operation!"

print(f"{first} {op} {second} = {result}")