# This project is for generating a flashcards to review
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
def main():
    file_name = "flashcard.txt"

    #with open creates a new text file. if the file exists then it updates it
    # open the file in write mode
    with open(file_name, 'w') as file:
        # write contetnt to the file
        file.write("Hello world ?")
    #print that the file is created
    print(f"file {file_name} created")

# call the main function
main()
