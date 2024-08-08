import os

def File_handling_task():
    file_path = r"C:\Users\prasanth.mm\Pictures\CP-Assignment-Task\AssignmentTask\Python\Assessment(23-07-24)\oops task\07-08-2024\demo.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            Available_word = content.split()
                
        search_word = input("Enter the search word: ")

        if search_word in Available_word:
            return f"The word '{search_word}' is present in the file."
        else:
            return f"The word '{search_word}' is not present in the file."
    else:
        return "The file does not exist."

print(File_handling_task()) 