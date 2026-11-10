num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose your operation: ")
match operation:
    case "+":
         print(num1 + num2)
    case "-":
         print(num1 - num2)
    case "*":
         print(num1 * num2)
    case "/":
         print(num1 / num2)
for i in range(1,11):
    print(i)