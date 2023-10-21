                  ## Calculator Project

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y



def main():
    while True:
        print("Welcome to Calculator\n")
        print("Select Your Operation:")
        print("1  Addition")
        print("2  Subtraction")
        print("3  Multiplication")
        print("4  Division")
        print("5  Exit\n")

        ch = input("Enter Your Choice: ")

        if ch == "1":
            while True:
                x = input("Enter first number: ")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            while True:
                y = input("Enter second number: ")
                if y.isdigit():
                    y = int(y)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            result = add(x, y)
            print(f"{x} + {y} = {result}\n")
        elif ch == "2":
            while True:
                x = input("Enter first number: ")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            while True:
                y = input("Enter second number: ")
                if y.isdigit():
                    y = int(y)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            result = subtract(x, y)
            print(f"{x} - {y} = {result}\n")
        elif ch == "3":
            while True:
                x = input("Enter first number: ")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            while True:
                y = input("Enter second number: ")
                if y.isdigit():
                    y = int(y)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            result = multiply(x, y)
            print(f"{x} * {y} = {result}\n")
        elif ch == "4":
            while True:
                x = input("Enter numerator: ")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            while True:
                y = input("Enter denominator: ")
                if y.isdigit():
                    y = int(y)
                    break
                else:
                    print("Invalid input. Please enter an integer.")
            if y == 0:
                print("Division by zero is not allowed.")
            else:
                result = divide(x, y)
                print(result, "\n")
        elif ch == "5":
            print("Exiting the Calculator. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.\n")

if __name__ == "__main__":
    main()

