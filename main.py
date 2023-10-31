# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def main():
    file = open("Input/Names/Invited_names.txt", "r")
    names = file.read().splitlines()
    file.close()
    file = open("Input/Letters/starting_letter.txt", "r")
    letter = file.read()
    for name in names:
        new_letter = letter.replace("[name]", name)
        letter_to_save = open(f"Output/ReadyToSend/letter_for_{name}.txt", "w")
        letter_to_save.write(new_letter)




main()