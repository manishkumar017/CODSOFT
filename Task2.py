

def calculator():
    print("Welcome to the Simple Calculator!")
    
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    
    print("\nSelect operation:")
    print("Add (+)")
    print("Subtract (-)")
    print("Multiply (*)")
    print("Divide (/)")

    operation = input("Enter the operation  (+, -, *, /): ").strip()

    
    if operation in ['+']:
        result = num1 + num2
        op_symbol = '+'
    elif operation in ['-']:
        result = num1 - num2
        op_symbol = '-'
    elif operation in ['*']:
        result = num1 * num2
        op_symbol = '*'
    elif operation in ['/']:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        op_symbol = '/'
    else:
        print("Invalid operation selection.")
        return

    print(f"\nResult: {result}")


calculator()



