# importing null_checker
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


# function that validates and returns the string input
def string_checker(question, valid_responses):
    while True:
        inp = null_checker(question).lower()

        for item in valid_responses:
            if inp == item or inp == item[:1]:
                return item

        print(f"Please choose between {valid_responses}\n")


# testing code
for i in range(5):
    print("You chose", string_checker("yes / no\n", ["yes", "no"]))
