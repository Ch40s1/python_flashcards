# This project is for generating a flashcards to review
# the point is to view flashcards from terminal where most of the work is done
# I also want to make it only using the python docs
# It generates a txt file and with the flashcards having a format of
# --------------------------------------------------------
# module name: sys
# description
# usage
# my example
# --------------------------------------------------------
# start:
# create a file with the format .txt
from pathlib import Path
import json


class Flashcard:
    current_id = 0

    def __init__(self, module_name, description):
        self.module_name = module_name
        self.description = description
        self.id = Flashcard.current_id
        Flashcard.current_id += 1

    def create_card(self):
        card_string = f"---------------card_id:{self.id}------------------\n"
        card_string += f"Description: {
            self.description}\nModule Name: {self.module_name}\n"
        card_string += f"---------------------------------\n"
        return card_string

    def delete_card(self):
        pass

    def to_json(self):
        flashcard = {
            "id": self.id,
            "python": True,
            "category": "OOP",
            "module_name": self.module_name,
            "description": self.description
        }
        return json.dumps(flashcard, indent=4)


def create_flashcard():
    module_name = input("Enter the module name: ")
    description = input("Enter the description: ")
    flashcard = Flashcard(module_name, description)
    return flashcard


def save_flashcard(file_name, flashcard):
    with open(file_name, 'a') as file:
        file.write(flashcard.to_json() + "\n")


def main():
    file_name = "flashcard.json"
    file_path = Path(file_name)

    if file_path.exists():
        print("File already exists :)")

        while True:
            print("1. Create a flashcard")
            print("2. Delete a flashcard")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                flashcard = create_flashcard()
                save_flashcard(file_name, flashcard)
                print("Flashcard created successfully.")

            elif choice == "2":
                if file_path.exists():
                    file_path.unlink()
                    print("Flashcard deleted successfully.")
                else:
                    print("No flashcard to delete.")

            elif choice == "3":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")
    else:
        print("Initial file does not exist, creating JSON file.")
        print("Run command again when file created.")
        flashcard = Flashcard("Example Module", "Example Description")
        with open(file_name, 'w') as file:
            file.write(flashcard.to_json() + "\n")
        print(f"File {file_name} created at project_name/flashcard.json")


# Call the main function
main()
