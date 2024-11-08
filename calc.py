def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1,num2):
    print(num1*num2)  

def division(num1,num2):
    print(num1/num2)       

x = input('Enter first operand: ')
y = input('Enter second operand: ')
result = add(x, y)
print("Addition:", result)

result = subtract(5, 3)
print("Subtraction:", result)

result = multiplication(5, 3)
print("Subtraction:", result)

result = division(5, 3)
print("Subtraction:", result)

