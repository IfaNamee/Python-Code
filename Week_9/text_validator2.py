def main():
    input_text = input("Please enter a title for validation & correction: ")

    while not input_text.replace(' ', '').isalpha():
        input_text = input("Try again, and enter a title: ")

    words = input_text.split()
    corrected_name = ""

    for i, word in enumerate(words):
        if i == 0:
            corrected_name += word.capitalize()  # Capitalize the first word
        else:
            # Words to keep in lowercase
            common_lowercase_words = ["and", "the", "of", "in", "on", "at", "for", "to"]
            if word.lower() in common_lowercase_words:
                corrected_name += " " + word.lower()  # Keep specified words in lowercase
            else:
                corrected_name += " " + word.capitalize()  # Capitalize other words

    return corrected_name


print("Welcome to the title validation program.")
corrected_name = main()
print("The corrected title is:", corrected_name)
