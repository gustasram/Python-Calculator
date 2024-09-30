"""Function allows the user to enter the needed math symbol for the equation."""

def input_math_symbol():
    math_sign = input("Input math symbol (+ - * / ^ or 'q' to quit): ")
    while math_sign not in ["+", "-", "*", "/", "^", "q"]:
        print("Invalid input!")
        math_sign = input("Input math symbol (+ - * / ^ or 'q' to quit): ")
    return math_sign