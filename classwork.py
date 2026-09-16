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