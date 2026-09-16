import math
import random
from fractions import Fraction
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

# string = "hello World is a common term in programming"
# print(string.count("m"))

# string = "hello World is a common term in programMMing"
# print(string.casefold())


# string = "***hello World is a common term in programming***"
# print (string.center(70))


# Numbers: integers, floats, complex numbers, mathematical operations 
# +, -, * , /, //, %, **

# comp1 = 5+2j
# comp2 = 4+6j
# print(comp1 + comp2)
# print(comp1 + 5)

# num = 10
# rad = math.radians(num)
# print(math.cos(rad))
# print(math.sin(rad))
# print(math.tan(rad))


# num = 10
# print(math.pi)
# rad = math.radians(num)
# print(math.cos(rad))
# print(math.sin(rad))
# print(math.tan(rad))

# print(math.factorial(5))
# print(math.lcm(20, 8))
# print(math.gcd(20, 8))
# print(math.pow(2, 3))
# print(math.floor(5/2))
# print(math.ceil(5/2))

# rand = random.randint(1, 10)
# print(random)
# print(random.choice(["Hello", "Hi", "Hey"]))
# print(random.sample(["Hello", "Hi", "Hey", 3, 4, 5], k=2))
# print(random.uniform(1, 10))
# print(random.choices(["Hello", "Hi", "Hey", 3, 4, 5], k=2))
# list1 = ["Hello", "Hi", "Hey", 3, 4, 5]
# print(random.shuffle(list1))
# print(list1)
# fac = Fraction(5/2)
# print(fac)


# BOOLEAN: logical operations, conditional statements , comparison
# print(1==1)
# print(1==11)


# is_student = True
# name = "Emmanuel"

# conditonal statements
# if is_student:
#     print(f"{name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 


       
# is_student = bool(input("Are you a student:"))
# name = "Emmanuel"

# if is_student == True:
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 


    
# is_student = bool(input("Are you a student:"))
# name = input("Enter your name:")
    
# if is_student == True:
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 




# is_student = bool(input("Are you a student:"))
# name = input("Enter your name:")
    
# if is_student != True:
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student") 


# logical statements     

# is_student = bool(input("Are you a student:"))
# name = input("Enter your name:")
    
# if is_student == True or name=="emmanuel":
#     print(f"Hello {name}, you are a student")
# else:
#     print(f"Hello {name}, you are not a student")    


# name = input("What is your name:")
# age = input("How old are you:")
# school = input("What school do you attend:")
# course = input("Which course do you offer:")
# state = input("Which state are from:")

# print(f"My name is {name} and I am {age} years old, I do attend {school}, and I offer {course} as my course, and my state of origin is {state}.")






# first_number = int(input("Enter your first number:"))
# second_number = int(input("Enter your second number:"))

# add = first_number + second_number
# sub = first_number - second_number
# mul = first_number * second_number
# div = first_number / second_number
# mod = first_number % second_number
# exp = first_number ** second_number

# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)
# print(exp)




# string = "=====MY PROFILE====="
# print (string.center(50))
# name = "name:Emmanuel"
# age = "age:18"
# country = "country:Nigeria"
# favorite_course = "favorite_course:python"
# print(name)
# print(age)
# print(country)
# print(favorite_course)
# string = "====================="
# print (string.center(5))





# Shopping Receipt Program

# # User input
# product_name = input("Enter the product name: ")
# price = float(input("Enter the price of the product: "))
# quantity = int(input("Enter the quantity purchased: "))
# discount_percent = float(
#     input("Enter discount percentage (e.g., 10 for 10%): ")
# )

# # Calculations
# total_cost = price * quantity
# discount_amount = (discount_percent / 100) * total_cost
# final_amount = total_cost - discount_amount

# # Display receipt
# print("\n" + "=" * 30)
# print(f"{'RECEIPT':^30}")
# print("=" * 30)
# print(f"Item: {product_name}")
# print(f"Price per unit: ${price:.2f}")
# print(f"Quantity: {quantity}")
# print(f"Subtotal: ${total_cost:.2f}")
# print(f"Discount ({discount_percent:.1f}%): -${discount_amount:.2f}")
# print("-" * 30)
# print(f"Total Amount Due: ${final_amount:.2f}")
# print("=" * 30)




# Age Category and Eligibility Program

# Get user input
age = int(input("Enter your age: "))

# Determine age category using if/elif/else
if age < 13:
    category = "Child"
elif 13 <= age <= 17:
    category = "Teenager"
elif 18 <= age <= 59:
    category = "Adult"
else:
    category = "Senior Citizen"

# Determine eligibility using comparison operators and boolean logic
can_vote = age >= 18
can_drive = age >= 18

# Convert boolean results to "Yes"/"No" strings
voting_eligibility = "Yes" if can_vote else "No"
driver_eligibility = "Yes" if can_drive else "No"

# Display results
print(f"Category: {category}")
print(f"Voting eligibility: {voting_eligibility}")
print(f"Driver's licence eligibility: {driver_eligibility}")