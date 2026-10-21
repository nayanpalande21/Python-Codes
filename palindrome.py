word = input("Enter a word:")

reverse = word[::-1]
if word == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#madam → Palindrome
#level → Palindrome
#python → Not a palindrome
#blockchain → Not a palindrome
#The words which are read from start to end / end to start have same meaning or letters or spelling are called as palindrome for example nayan from both the end the letters,spelling,meaning is the same so it is a palindrome.
#The words which are read from start to end has different meaning and from end to start when read has different spellings,letters,meaning are not called as a palindrome for example python from start to end has different meaning,spelling and from end to start has a different meaning,spelling so it is not a palindrome.
#List: append() adds an item.
#Set: add() adds an item.