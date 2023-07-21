# Null Checker for String Inputs
def null_checker(question):
    while True:
        try:

            inp = input(question)

            if inp.strip() == "":
                raise ValueError
            else:
                return inp

        except:
            print("Please do not leave this blank\n")


# Main Routine for Testing
for i in range(1, 5):
    print("Hi,", null_checker("Please enter your name\n"))
