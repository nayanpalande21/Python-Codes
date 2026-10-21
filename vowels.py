words = input("Enter the word: ")
count = 0

for letter in words.lower():
    if letter in "aeiou":
        count += 1

print("Number of vowels:", count)

word = input("Enter the word:")
reverse = 0 
for letter in words.lower():
    reverse= word[::-1]
print("Reversed word:")