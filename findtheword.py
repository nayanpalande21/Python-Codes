sentence = input("Enter a sentence: ")
word = input("Enter a word to find: ")

if word.lower() in sentence.lower():
    print("Word found!")
else:
    print("Word not found!")


    # A. word.lower()=Converts the searched word to lowercase."Python" becomes "python".
    # B. sentence.lower()=Converts the entire sentence to lowercase."I love learning Python" becomes "i love learning python".
    # C. in=Checks whether the word exists inside the sentence."python" in "i love learning python" evaluates to True.