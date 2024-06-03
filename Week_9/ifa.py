

def inputs():
    feedback = input("Enter as many words as you like. You don't have to capitalize: ")

    while not feedback.replace(' ', '').endswith('!'):
        feedback = input("Enter a word that ends with a '!': ")

    words = feedback.split()
    feedbacks = " "

    for i, words in enumerate(words):
        if i == 0:
            feedbacks += words.capitalize()
        else:
            lowercase_words = [" "]
            if words.lower() in lowercase_words:
                feedbacks += " " + words.lower()
            else:
                feedbacks += " " + words.capitalize()

    return feedbacks


ifa = inputs()
print("You entered:", ifa)
print(f': {ifa.strip()}')
