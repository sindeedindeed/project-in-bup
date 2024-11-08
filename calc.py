def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return int(num1 * num2)

def division(num1, num2):
    return int(num1 / num2)

x = int(input('Enter first operand: '))
y = int(input('Enter second operand: '))

result = add(x, y)
print("Addition:", result)

result = subtract(x, y)
print("Subtraction:", result)

result = multiplication(x, y)
print("Multiplication:", result)

result = division(x, y)
print("Division:", result)


