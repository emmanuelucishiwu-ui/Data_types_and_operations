# course = input("Enter your course name:")
# string = f"I am studying {course}"
# print(string)


# course = input("Enter your course name: ")
# age = input("Enter your age:")

# string = "I am {a} years old and I am studying {k} ".format(a=age, k=course)
# print(string)


# string escape sequences
#   - \n: newline
#   - \t: tab
#   - \b: backspace
#   - \r: carriage return
#   - \f: form feed
#   - \": double quote
#   - \': single quote
#   - \\: backslash

# string = "I am \"20 years old and I am studying java\""
# print(string)

# string = "I am \"20 years old \n and I am studying java\""
# print(string)

# string = "I am \"20 years old \: and I am studying java\""
# print(string)

# no = 100000000
# string = f"I am {no:,} years old \\ and I am studying java"
# print(string)



# name = "Emmanuel"
# age = 18
# course = "Java"

# sentence = f"My name is {name}, I am {age} years old, and I study {course}."
# print(sentence)


# money = 2500000
# print(f"I have ₦{money:,}.")


# price = 1500
# print(f"The price is ₦{price:,.2f}.")


# score = 0.875
# print(f"My score is {score:.1%}.")


# message = f"Name: {name}\nAge: {age}\nCourse: {course}\n\tWelcome!"
# print(message)

# print("New line: \n")
# print("Tab space: \tHello")
# print("Backslash: \\")
# print("Double quote: \"Hello\"")
# print("Single quote: \'Hello\'")


# what is indexing 

# indexing is the process of accessing an individual elements
# within a sequence-such as a string, list 
# or tupple-by referring to 
# its specific postion number

# string = "Hello a World"
# print(string[0])

# string = "Hello World is a common programming term"
# print(string.find("p"))

# text = "Ishiwu Emmanuel"
# print(text[0])
# print(text[14])


# slicing 
#  slicing accessing a portions of s sequence


# string = "Hello a World"
# print(string[0:5])

# string = "Hello World is a common term in programming"
# print(len(string))
# print(string[0:-1:2])
# print(string[-43])


# methods
# method is a function that belongs to a specific object or class

# capitalize() casefold() center() count()
# endwith() find() format() index() 
# isalpha() isdigit() join() lower() replace() split() strip()

string = "hello World is a common term in programming"
print(string.count("m"))