import PyPDF2


def decrypt_pdf(pdf_path, dictionary_path):
    # Load the dictionary file
    with open(dictionary_path, 'r', encoding='utf-8') as dictionary_file:
        words = [word.strip() for word in dictionary_file]

    # Try each word as a password
    for word in words:
        # Try both uppercase and lowercase forms of the word
        for case in [word, word.lower()]:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                if pdf_reader.decrypt(case) == 1:
                    print(f"Password found: {case}")
                    return

    print("Password not found in the dictionary.")


if __name__ == "__main__":
    # Replace 'encrypted.pdf' and 'dictionary.txt' with your actual file paths
    pdf_path = 'encrypted.pdf'
    dictionary_path = 'dictionary.txt'
    decrypt_pdf(pdf_path, dictionary_path)
