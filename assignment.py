# methods
# method is a function that belongs to a specific object or class

# capitalize() casefold() center() count()
# endwith() find() format() index() 
# isalpha() isdigit() join() lower() replace() split() strip()


# for count
string = "hello World is a common term in programming"
print(string.count("m"))

# endswith
string = "hello World is a common term in programming"
print(string.endswith("g"))
# endwith shows that if it ends with g is true if it's not is 

# find
string = "hello World is a common term in programming"
print(string.find("m"))
# find where the m is postioned

# format
name = "Emmanuel"
age = 18
print("my name is {} and i am {} years old". format(name , age))
# format is used to print everything in strings

# Index 
string = "hello World is a common term in programming"
print(string [0])
# it is used to locate the postion pfstion a number 

# isalpha
string = "hello World is a common term in programming"
print(string.isalpha())
string = "Emmanuel"
print(string.isalpha())
string = "emmanuel23"
print(string.isalpha())
# in this isalpha when you type in a string without a space or
# a number it will show true but when you do it will show false
# 
# isdigit
string = "234"
print(string.isdigit())
string = "234emmanuel"
print(string.isdigit())
string = "234 77"
print(string.isdigit())
# as for the isdigit it is the oppostite of isalpha but this one 
# deals with numbers, it say true when it is only numbers, and say 
# false when it has space or has a letter in it 

# join
string =["I", "love", "this", "snack", "very", "much"]
result = " " .join(string)
print(result)
# the join connects word together 

# lower
string = "HELLO EMMANUEL"
print(string.lower())
# it convert higher case to lower case

# replace 
string = "i like helicopter"
print(string.replace("helicopter", "private_jet"))


# split
string = "benz, toyta, bmw"
print(string.split(","))


# strip
string = "***i am a student***"
print(string.strip("*"))
# the strip just remove what is covering it and then print


 