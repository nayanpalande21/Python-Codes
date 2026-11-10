# #List: append() adds an item.
# #Set: add() adds an item.
# # single line comment
# '''   multi-line comment       '''
# # \n is used for new-line 
# # \\ is used for this or that for example- print("This can be done good\\better")  output- This can be done good\better 
# # \ is an escape sequence character
# # \" is used to print " in the between the strings or words for example- print("Hello \" World ") output- Hello " World
# # string can be displayed using "Hello" , 'Hello'  for example - print('Hello World',"Nayan") 
# #                                                                          (arguments)
# #sep stands for space between the strings,arguments.We can also set the value for space for example - print('Hello World',"Nayan", sep="\" ) output = Hello World\Nayan
# # end is a by default \n newline .Just a user can use it to end its string with the characters he want to for example - print("Hello World" , end = "..") output= Hello World ..
# #REPL - READ EVALUATE PRINT LOOP (RUN PYTHON IN A TERMINAL AND CAN START EXECUTING COMMANDS FROM THERE AND THIS IS CALLED RAPPEL )
# # 1. Arithmetic Operators- Addition(+),Subtraction(-), Multiplication(*),Division(/),Module(%),Exponentiation(** , square of that number eg= 34*34=1156),Floor Division(//)
# # Assignment operator (=) used to assign value to a variable a= 6
# # (==) means is a equal to 10 print(10 == 6)
# # 2. Conditional Operator- Equal(==),Not Equal(!=), GreaterThan(>),LessThan(<),GreaterThan or Equal(>=),LessThan or Equal(<=)
# #Logical Operator- and(&),or,not
# #True AND True  = True ,         True OR True = True,           True NOT = False
# #True AND False = False,         True OR False= True,           False NOT = True
# #False AND True = False,         False OR True= True,
# # False AND False = False        False OR False= False,

# # 3. Assignment Operator- [=,+=,-=,/=,%=,*=,//=]
# # Conditional Statements - if ;if-else; if-elif-else 
# # match-case is a new feature introduced in python 3.10 for pattern matching it is similar to if-elif-else but in few programs for example for a lucky-draw we use match-case to directly print the output 
# #    syntax for match-case is as follows:
# #                              match value:
# #                              case pattern1: (code to execute if value matches the pattern)
# #                              case pattern2: (code to execute if value matches the pattern)
# #                              case _: (default case if no patterns match)
# # crtl+/ for multiple single line comment 
# # while loop - it executes a block of code as long as a condition is true.They are useful when the number of iterations is not known in advance.
# # Syntax = while condition:
# #     (code to execute while condition is true )
# # Example = count = 0

# # while count < 5:
# #     print(count)
# #     count += 1
# # Infinite Loops: Be careful to avoid infinite loops by ensuring the condition eventually becomes False.
# # Example of an infinite loop:
# #                  while True:
# #                   print("This will run forever!")
# #break- it will no longer will be executed,cancel the execution of this loop now.
# #continue - continue the loop for the next iteration here itself . It skips the rest of the code in the current iteration and moves to the net iteration.
# #Example - for i in range(5):
#  # if i == 2:
#  #     continue    
#  # print(i)  # Output: 0, 1, 3, 4
#  # pass - do nothing(The pass statement is a placeholder that does nothing. It is used when syntax requires a statement but no action is needed.) 
#  #Example - for i in range(5):
# # if i == 3:
# #     pass  # Do nothing
# # print(i)  # Output: 0, 1, 2, 3, 4
# # '' used to represent a string 
# # "" used to represent a string
# # '''''' used to represent a multiline string 
# # for single line string use '' or "" 
# # in programming the indexing start from 0
# # strings are immutable
# # capitalize() converts the 1st letter of a word in to Upper-case
# # upper() converts the letters of string in upper case
# # lower() converts the letters of string in lower case
# # text = "hello world"
# # print(text.upper())  # Output: "HELLO WORLD"
# # print(text.lower())  # Output: "hello world"
# # print(text.title())  # Output: "Hello World"
# # print(text.capitalize())  # Output: "Hello world"
# # text = "  hello world  "
# # print(text.strip())  # Output: "hello world"
# # print(text.lstrip()) # Output: "hello world  "
# # print(text.rstrip()) # Output: "  hello world"
# # text = "Python is fun"
# # print(text.find("is"))   # Output: 7
# # print(text.replace("fun", "awesome"))  # Output: "Python is awesome"
# # text = "Python is fun"
# # print(text.find("is"))   # Output: 7
# # print(text.replace("fun", "awesome"))  # Output: "Python is awesome"
# # text = "apple,banana,orange"
# # fruits = text.split(",")
# # print(fruits)  # Output: ['apple', 'banana', 'orange']

# # new_text = " - ".join(fruits)
# # print(new_text)  # Output: "apple - banana - orange"
# # text = "Python123"
# # print(text.isalpha())  # Output: False
# # print(text.isdigit())  # Output: False
# # print(text.isalnum())  # Output: True
# # print(text.isspace())  # Output: False
# # text = "Hello, Python!"
# # print(len(text))  # Output: 14
# # print(ord('A'))  # Output: 65
# # print(chr(65))   # Output: 'A'
# # To check whether a string is alphabatical use syntax- print(str1.isalpha())
# # To check whether a string is alphanumberic use syntax- print (str1.isalnum())
# # Recursion is function calling itself
# #Why to use recursion bcoz it directly solves the problem.
# #Fibonacci series is a sequence of numbers where each number is the sum of the two numbers before it 
# # example = 0+1 = 1 , 1+1=2, 1+2=3, 2+3=5
# #     0 1 1 2 3 5 
# # 2 types of modules in Python:
# # - Build in Modules - Built-in modules are modules that come with Python. We don't need to install them separately. We can directly import and use them.
# # - External Modules - External modules are modules developed by third-party developers. They are not included in the standard Python installation and generally need to be installed separately using pip.
# # Command	Purpose
# pip install requests	Installs an external module
# python -m pip install requests	Installs using the pip associated with that Python interpreter
# import requests	Imports the installed module
# requests.__version__	Displays its version 