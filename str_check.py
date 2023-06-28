from null_check import null_checker

# String Checker for Instructions Component


def string_checker(question, valid_responses):
    while True:

        inp = null_checker(question).lower()

        for item in valid_responses:
            if inp == item or inp == item[:1]:
                return item

        print(f"Please choose between {valid_responses}\n")


# Main Routine for Testing
print(string_checker("yes / no\n", ['yes', 'no']))
