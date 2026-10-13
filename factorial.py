num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative integers")
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial:", factorial)