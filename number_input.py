"""The number input function allows to take and store the number from a user."""

def input_number():
    while True:
        user_input = input("Input a number (or 'q' to quit): ")
        if user_input == 'q' or user_input == 'clear':
            return user_input
        try:
            user_number = int(user_input)
        except ValueError:
            print("You must enter a number (or 'q' to quit)!")
        else:
            return user_number
    