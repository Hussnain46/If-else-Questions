"""     1) Basic If-Else Usage:
Write a program that takes an integer input from the user. 
If the number is even, print "Even", 
otherwise print "Odd"."""

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



"""     2) Simple Login System:
Create a program with username "admin" and password "12345". 
Ask the user to enter username and password. 
If both are correct, print "Login successful"; 
otherwise, print "Login failed"."""

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# username_in_db = "admin"
# paswrd_in_db = 12345
# if username == username_in_db or password == paswrd_in_db:
#     print("Login Successful")
# else:
#     print("Login Failed")



"""     3) Grading System:
Write a Python program that asks for a student's mark (between 0 and 100). 
If the mark is below 50, print "Fail"; 
if the mark is between 50 and 60, print "Pass"; between 61 and 75, print "Good"; 
between 76 and 90, print "Very Good"; and above 90, print "Excellent"."""

# marks = int(input("Enter your marks (between 0 to 100): "))
# if 0 <= marks < 50 :
#     print("Fail")
# elif 50 <= marks <=60:
#     print("Pass")
# elif 61 <= marks <=75:
#     print("Good")
# elif 76 <= marks <= 90:
#     print("Very Good")
# elif 91 <= marks <= 100:
#     print("Excellent")
# else:
#     print("Invalid Input. Please Write numbers in between 0 to 100 ")




"""     4) Nested If-Else (Age and Driving License):
Write a program that asks the user their age. 
If the user is less than 18, print "You are too young to drive". 
If the user is 18 or older, ask if they have a driving license (yes/no). 
If they have one, print "You can drive"; otherwise, print "You need a driving license to drive"."""


# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are too young to drive. ")
# else:
#     d_licnce = input(" Do you have a driving license (yes/no): ").lower()
#     if d_licnce == "yes":
#         print("You can drive. ")
#     elif d_licnce == "no":
#         print("You need a driving license to drive. ")
#     else:
#         print("Invalid Input. Please enter 'yes' or 'no'. ")




"""     5) Temperature Advice:
Write a program that asks the user for the current temperature. 
If the temperature is below 0, print "It's freezing—consider staying home". 
If it is between 0 and 18, print "It's cold—wear warm clothes". 
If it is between 19 and 35, print "Nice weather today". 
If the temperature is above 35, print "It's hot—stay hydrated"."""

# temp = int(input("Enter your current Temprature: "))
# if temp < 0:
#     print("It's freezing—consider staying home. ")
# elif temp >= 0 and temp <= 18:
#     print("It's cold—wear warm clothes")
# elif 19 <= temp <=35:
#     print("Nice weather today")
# elif temp > 35:
#     print("It's hot—stay hydrated")



"""     6) Handling Different User Input Types:
Write a program where a user can type "start" or "stop". 
If the user types "start", print "Machine started"; 
if "stop", print "Machine stopped". 
For any other input, print "Unknown command"."""

# machine = input("Enter command of 'start' and 'stop': ").lower()
# if machine == "start":
#     print("Machine Started")
# elif machine == "stop":
#     print("Machine Stopped")
# else:
#     print("Unknown Command")



"""     7) Eligibility for Voting:
Ask the user to enter their age. 
If the age is less than 18, print "You are not eligible to vote yet". 
If 18 or older, print "You are eligible to vote". 
Use the pass statement to handle the condition where the user is exactly 18."""

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are not eligible to vote yet")
# elif age == 18:
#     pass
# else:
#     print("You are eligible to vote")




"""     8) Simple Calculator:
Create a program that asks the user to enter two numbers and 
a choice of operation (add, subtract, multiply, divide). 
Use nested if-else statements to perform the operation and print the result. 
If the user chooses "divide" and the second number is 0, print "Cannot divide by zero"."""

# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a second number: "))
# calculate = input("Enter a opteration in (add, substract, multiply, divide): ").lower()

# if calculate == "add":
#     result = num1 + num2
#     print("Result:",result)
# elif calculate == "substract":
#     result = num1 - num2
#     print("Result:", result)
# elif calculate == "multiply":
#     result = num1 * num2
#     print("Result:", result)
# elif calculate == "divide":
#     if num2 == 0:
#         print("Cannot divide by zero")
#     else:
#         result = num1 / num2
#         print("Result:",result)
# else:
#     print("Invalid operation. Please choose add, subtract, multiply, or divide.")




"""     9) Discount System Based on Purchase Amount:
Write a program that asks the user for their total purchase amount. 
If the amount is over $500, they get a 20% discount; 
between $200 and $500, a 10% discount; and for less than $200, a 5% discount. 
Print the final amount after discount."""

# amount = float(input("Enter your total purchase amount: "))
# if amount > 500:
#     discount = 0.20  
# elif 200 <= amount <= 500:
#     discount = 0.10
# else:
#     discount = 0.05

# dis_amount = amount * (1 - discount)
# print(f"Final amount after discount: {dis_amount:.2f}")



"""     10) Leap Year Checker:
Write a program that asks the user to input a year and checks whether 
it is a leap year. A year is a leap year if it is divisible by 4, 
except for years that are divisible by 100, unless they are also divisible by 400."""

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")




"""     11) Sorting Three Numbers:
Ask the user to enter three different numbers. 
Write a program that will print these numbers in ascending order without using lists or sort functions. 
Use nested if-else statements."""

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 <= num2 and num1 <= num3:
#     smallest = num1
#     if num2 <= num3:
#         middle = num2
#         largest = num3
#     else:
#         middle = num3
#         largest = num2
# elif num2 <= num1 and num2 <= num3:
#     smallest = num2
#     if num1 <= num3:
#         middle = num1
#         largest = num3
#     else:
#         middle = num3
#         largest = num1
# else:
#     smallest = num3
#     if num1 <= num2:
#         middle = num1
#         largest = num2
#     else:
#         middle = num2
#         largest = num1

# print(f"{smallest} {middle} {largest}")



"""     12) Day Schedule Program:
Write a program that asks the user to input the day of the week. 
Depending on the day, print different activities 
(e.g., Monday - Coding, Tuesday - Meeting, etc.). 
Include a message for weekends saying "Time to relax!" and 
for invalid inputs, provide an error message."""

# day = input("Enter the day of the week: ").lower()

# if day == "monday":
#     print("Monday - Coding")
# elif day == "tuesday":
#     print("Tuesday - Meeting")
# elif day == "wednesday":
#     print("Wednesday - Gym")
# elif day == "thursday":
#     print("Thursday - Project work")
# elif day == "friday":
#     print("Friday - Team dinner")
# elif day == "saturday" or day == "sunday":
#     print("Time to relax!")
# else:
#     print("Invalid input. Please enter a valid day of the week.")




"""     13) Complex Number Classification:
Create a program that takes two integers, representing the real and 
imaginary parts of a complex number. 
Classify the number as purely real, purely imaginary, or neither, and print the result."""


# real_part = int(input("Enter the real part of the complex number: "))
# imag_part = int(input("Enter the imaginary part of the complex number: "))

# if real_part == 0 and imag_part == 0:
#     print("The complex number is not purely real nor purely imaginary.")
# elif real_part == 0:
#     print("The complex number is purely imaginary.")
# elif imag_part == 0:
#     print("The complex number is purely real.")
# else:
#     print("The complex number is neither purely real nor purely imaginary.")



"""     14) Age Group Categorization:
Write a program that takes the user's age and categorizes them 
into different age groups: 0-12 "Child", 13-19 "Teenager", 20-35 "Young Adult", 
36-55 "Adult", 56+ "Senior". For each category, print an appropriate message."""

# age = int(input("Enter your age: "))

# if 0 <= age <= 12:
#     print("Child.")
# elif 13 <= age <= 19:
#     print("Teenager.")
# elif 20 <= age <= 35:
#     print("Adult.")
# elif 36 <= age <= 55:
#     print("Adult.")
# elif age >= 56:
#     print("Senior.")
# else:
#     print("Invalid age entered.")






"""     15) Check Multiple Conditions:
Ask for three inputs from the user: age, a boolean indicating 
if they are a student, and another boolean indicating if they have a scholarship. 
Use nested conditions to determine if they get a discount on software purchase. 
Rules: Under 18 or a student gets 20% off; students with scholarships get an additional 10% off."""

# age = int(input("Enter your age: "))
# student = input("Are you a student? (yes/no): ").lower()
# scholarship = input("Do you have a scholarship? (yes/no): ").lower()

# if student == 'yes':
#     is_student = True
# else:
#     is_student = False

# if scholarship == 'yes':
#     has_scholarship = True
# else:
#     has_scholarship = False

# if age < 18 or is_student:
#     discount = 20

#     if has_scholarship:
#         discount += 10
# else:
#     discount = 0

# print(f"You will get a {discount}% discount on the software purchase.")



"""     16) Fitness Level Tester:
A program prompts the user for the number of push-ups and sit-ups they can perform. 
If the user can do more than 40 push-ups and more than 50 sit-ups, print "High fitness level". 
If they can do 20 to 40 push-ups and 30 to 50 sit-ups, 
print "Average fitness level". Otherwise, print "Low fitness level"."""

# push_ups = int(input("Enter the number of push-ups: "))
# sit_ups = int(input("Enter the number of sit-ups: "))

# if push_ups > 40 and sit_ups > 50:
#     print("High fitness level")
# elif 20 <= push_ups <= 40 and 30 <= sit_ups <= 50:
#     print("Average fitness level")
# else:
#     print("Low fitness level")



"""     17) Traffic Light Simulator:
Write a program that simulates traffic lights. 
The user inputs "green", "yellow", or "red". If "green", print "Go". 
If "yellow", print "Slow down". If "red", print "Stop". 
Include a check for invalid inputs, and use the exit() function to terminate if the input is "quit"."""


# while True:
#     traffic_light = input("Enter the traffic light color (green, yellow, red) or 'quit' to end: ").lower()

#     if traffic_light == 'quit':
#         print("Program End.")
#         break 

#     elif traffic_light == "green":
#         print("Go")
#     elif traffic_light == "yellow":
#         print("Slow down")
#     elif traffic_light == "red":
#         print("Stop")
#     else:
#         print("Invalid input. Please enter 'green', 'yellow', 'red', or 'quit'.")
