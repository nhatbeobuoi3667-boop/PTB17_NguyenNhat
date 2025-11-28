def addition():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return f"The answer is: {num1} + {num2} = {num1 + num2:.2f}"
    except ValueError:
        return "That is not a number"

def subtraction():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return f"The answer is: {num1} - {num2} = {num1 - num2:.2f}"
    except ValueError:
        return "That is not a number"

def multiplication():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return f"The answer is: {num1} x {num2} = {num1 * num2:.2f}"
    except ValueError:
        return "That is not a number"

def division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            return "Cannot divide by zero"
        return f"The answer is: {num1} : {num2} = {num1 / num2:.2f}"
    except ValueError:
        return "That is not a number"

def main():
    option = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Division",
        5: "Exit"
    }

    for i, x in option.items():
        print(f"{i}. {x}")

    while True:
        try:
            choose = int(input("Enter an option: "))

            if choose == 1:
                print(addition())
            elif choose == 2:
                print(subtraction())
            elif choose == 3:
                print(multiplication())
            elif choose == 4:
                print(division())
            elif choose == 5:
                print("Thank you for using my calculator!")
                break
            else:
                print("That is not a valid option")
        except ValueError:
            print("That is not a valid input")

if __name__ == '__main__':
    main()
