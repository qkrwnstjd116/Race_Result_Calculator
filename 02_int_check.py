# function that checks if the input is an integer within the given range
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


# testing code
for i in range(5):
    print("You chose", integer_checker("Enter a number between 1 to 10\n", 1, 10))
