def main():
    input_text = input("Please enter a full name for validation & correction: ")

    while not input_text.replace(' ', '').isalpha():
        input_text = input("Try again, and enter a full name: ")

    name = input_text.split()
    corrected_name = " "

    for i, name in enumerate(name):
        if i == 0:
            corrected_name += name.capitalize()  # Capitalize the first word
        else:
            common_lowercase_words = ["van", "de"]
            if name.lower() in common_lowercase_words:
                corrected_name += " " + name.lower()  # Keep specified words in lowercase
            else:
                corrected_name += " " + name.capitalize()  # Capitalize other words

    return corrected_name


print("Welcome to the text validation program.")
corrected_name = main()
print("The corrected full name is:", corrected_name)
