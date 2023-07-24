# function that takes input that is not blank
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


# testing code
for i in range(4):
    print("Hi,", null_checker("Please enter your name\n"))
