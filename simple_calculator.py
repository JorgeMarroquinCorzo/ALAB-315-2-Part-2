# simple_calculator.py

def main():
    print("Welcome to my calculator!")

   #  Ask for the first number repeatedly until valid
    while True:                                         # <--- This starts the loop 
        num1_input = input("Enter the first number: ")
        if num1_input.replace(".", "", 1).isdigit():
            break                                       # <--- This stops the loop immediately
        print("Error: Invalid numeric input. Please enter a valid number.")

    #  Ask for the second number repeatedly until valid
    while True:
        num2_input = input("Enter the second number: ")
        if num2_input.replace(".", "", 1).isdigit():
            break                                       # <--- This stops the loop immediately
        print("Error: Invalid numeric input. Please enter a valid number.")

    # Convert valid inputs to floats
    num1 = float(num1_input)
    num2 = float(num2_input)


    # Ask the user to choose an operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print(f"Error: '{operation}' is an unsupported operation symbol.")
        return

    # Clean up display if numbers are whole integers
    display_num1 = int(num1) if num1.is_integer() else num1
    display_num2 = int(num2) if num2.is_integer() else num2
    display_result = int(result) if isinstance(result, float) and result.is_integer() else result

    # Print the result
    print(f"{display_num1} {operation} {display_num2} = {display_result}")


if __name__ == "__main__":
    main()