num1 = float(input("Enter first number: "))
action = input("Enter '+', '-', '*' or '/': ")
num2 = float(input("Enter second number: "))

if action == '+':
    print(num1 + num2)

elif action == '-':
    print(num1 - num2)

elif action == '*':
    print(num1 * num2)

elif action == '/':
    print(num1 / num2)

else:
    print("Invalid operation entered")