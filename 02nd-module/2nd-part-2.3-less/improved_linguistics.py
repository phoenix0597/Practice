# There is a list of three words that the user enters.
# Then user enters some text by entering one word at time.
# The text is entered until the word "end" is encountered.
# Write a program that counts how many times the user's words occur in the text.
def count_word_occurrences():
    # the list of three words that the user enters
    words_list = []
    # count the number of times the user's words occur in the text
    counts = [0, 0, 0]
    # enter three words and store them in the list
    for num in range(3):
        word = input(f"Введите {num + 1}-е, слово: ")
        words_list.append(word.strip())

    # the text entered by the user step by step one word at time
    text = ""
    # first word entered by the user
    text_word = input("Слово из текста (или 'end' чтобы закончить): ")
    # other words, entered by the user step by step until the word "end" is encountered
    while text_word != "end":
        # as the word is entered, check if the word is in the list of given words
        # and increase the count of the word in the list of counts if the word is in the list of given words
        for i in range(3):
            if text_word.strip() == words_list[i]:
                counts[i] += 1
        text_word = input("Слово из текста (или 'end' чтобы закончить): ")
        text += text_word
    # print the result
    print("Подсчет слов в тексте:")
    for i in range(3):
        print(f"{words_list[i]}: {counts[i]}")


# call the function
count_word_occurrences()
