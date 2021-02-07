# Calculator in Python

def calculator():
    print("-----------------------")
    print("||||| Calculator |||||")
    print("-----------------------")

    print("+ For Addition")
    print("- For Subtraction")
    print("/ For Division")
    print("* For Multiplication")
    print("% For Modulus")

    number1 = int(input("\nEnter number one :"))
    operator = input("Enter your operator :")
    number2 = int(input("Enter number two :"))
    if operator == '+':
        formula = number1 + number2
        print("The sum of number one and number two is :",formula)
    elif operator =='-':
        formula = number1 - number2
        print("The subtraction of number one and number two is :",formula)
    elif operator =='/':
        formula = number1 / number2
        print("The division of number one and number two is :",formula)
    elif operator =='*':
        formula = number1 * number2
        print("The multiplication of number one and number two is :",formula)
    elif operator =='%':
        formula = number1 % number2
        print("The modulus of number one and number two is :",formula)
    else:
        print("Invalid operator.")

calculator()
