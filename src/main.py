# my vision is to create a program that will create a list of flashcards that will be accessible in a website and the terminal
# create a flashcard class that will be used to make more types later
class Flashcard:
    def __init__(self):
        pass
    # flashcards will have a name, description and example

# function that creates a flashcard and appends it to a json file


def main():
    # when ran display welcome and ask for several
    print("Welcome!")
    print("1. Create card(test), 2. Exit")
    # create a variable to keep the program running
    program_status = True
    while program_status:
        # ask user for input
        current_task = input("What would you like to do?")
        # check for task number
        if current_task == '2':
            program_status = False
            print("Goodbye :)")
        elif current_task == 1:
            print("Creating a new card!... in progress...")
        else:
            print("Please input a valid task.")


# Call the main function
main()
