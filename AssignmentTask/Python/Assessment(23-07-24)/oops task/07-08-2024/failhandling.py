import os

def File_handling_task():
    file_path = r"demo.txt"

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