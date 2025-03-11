def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operation"

            print("Result:", result)

            if input("Do you want to continue? (y/n): ").lower() != "y":
                break

        except ValueError:
            print("Invalid input, please enter numbers only.")

if __name__ == "__main__":
    calculator()
