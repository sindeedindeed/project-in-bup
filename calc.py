def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return int(num1 * num2)

def division(num1, num2):
    if num2 != 0:
        return int(num1 / num2)
    else:
        return "Error."    

print("Select operation: ")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")


Instruction = input("Input your operation number:")
x = float(input('Enter first operand: '))
y = float(input('Enter second operand: '))

if Instruction =='1':
    result = add(x, y)
    print("Addition:", result)

elif Instruction == '2':
    result = subtract(x, y)
    print("Subtraction:", result)

elif Instruction == '3':
    result = multiplication(x, y)
    print("Multiplication:", result)

elif Instruction == '4':
    result = division(x, y)
    print("Division:", result)

else:
    print("Invalid Input.")    

