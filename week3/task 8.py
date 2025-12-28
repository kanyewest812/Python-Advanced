n = int(input("n: "))

print("By all:")
for num in range(1, n + 1):
    vrem = num
    ok = True

    while vrem > 0:
        digit = vrem % 10
        if digit == 0 or num % digit != 0:
            ok = False
            break
        vrem //= 10

    if ok:
        print(num, end=" ")
print()


#task 8.2
def swapFnL(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]


m = int(input("Array length: "))
A = []

for i in range(m):
    A.append(int(input("Element: ")))

print("OG array:", A)

swapFnL(A)

print("Result array:", A)
