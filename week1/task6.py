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
    result = first / second
else:
    result = "Unknown operation!"

print(f"{first} {op} {second} = {result}")