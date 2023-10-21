# CalculatorProject

This Python script is a simple command-line calculator program that allows users to perform basic mathematical operations such as addition, subtraction, multiplication, and division. Here's a description of how the program works:

1. The program defines four functions for performing basic mathematical operations:
   - `add(x, y)`: Returns the sum of two numbers.
   - `subtract(x, y)`: Returns the result of subtracting the second number from the first.
   - `multiply(x, y)`: Returns the product of two numbers.
   - `divide(x, y)`: Performs division and returns the result. It includes a check to prevent division by zero.

2. The `main()` function is the entry point of the program and is wrapped in a while loop, allowing the user to perform multiple calculations.

3. Inside the `main()` function, a menu is displayed, and the user is prompted to select an operation or exit the calculator. The available options are:
   - 1: Addition
   - 2: Subtraction
   - 3: Multiplication
   - 4: Division
   - 5: Exit

4. The user is asked to input their choice (a number corresponding to the operation they want to perform).

5. Depending on the user's choice, the program guides the user through entering the required numbers for the selected operation.

6. For each operation (addition, subtraction, multiplication, or division), the program checks that the user's input is a valid integer before performing the calculation. If the user enters an invalid input, they are prompted to enter an integer again.

7. The program performs the selected operation and displays the result to the user.

8. If the user chooses division (option 4), there is an additional check to ensure that the denominator is not zero, as division by zero is not allowed.

9. If the user chooses to exit (option 5), the program displays a goodbye message and breaks out of the loop, ending the program.

10. If the user enters an invalid choice, the program informs them that the choice is invalid and prompts them to try again.

The program continues to run until the user chooses to exit. It provides a basic calculator functionality for performing simple mathematical operations in a text-based interface.
