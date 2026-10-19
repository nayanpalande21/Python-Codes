languages = ["C", "C++", "Java", "Solidity", "GO", "Python"]

languages.remove("C++")
print(languages)

languages.pop(2)
print(languages)

languages[languages.index("GO")] = "C++"
print(languages)