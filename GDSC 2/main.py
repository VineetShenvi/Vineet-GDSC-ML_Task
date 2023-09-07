expression= input("Enter an expression (or 'q' to quit): ")
expression = expression.replace(',', '')
expression = expression.replace(' ', '')
expression = expression.replace('x', '*')
expression = expression.replace('=', '')
expression = expression.replace('^', '**')

valid_characters = "+-?*/()."
try:
    for character in expression:
        if not (character in valid_characters or character.isnumeric()):
            raise ValueError("Invalid characters in the expression")

    result = eval(expression)
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as e:
    print(str(e))

