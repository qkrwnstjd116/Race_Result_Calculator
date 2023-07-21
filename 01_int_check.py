# Integer Checker
def integer_checker(question, min, max):
    while True:
        try:
            inp = int(input(question))

            if inp < min or inp > max:
                raise ValueError
            else:
                return inp

        except:
            print(f"Please enter an integer between {min} and {max}\n")


# Main Routine for Testing
for i in range(1, 7):
    print("You chose", integer_checker(
        "Enter a number between 1 to 10\n", 1, 10))
