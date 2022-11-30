# number = 0
# if number < 0:
#     print("the number is negative") # this will print nothing because the number is equal to 0


# number = -4
# if number < 0:
#     print("the number is negative") # this will print our statement because the number is true (less than 0)

# if number > 0:
#     print("the number is positive") # this will not execute because it's false (the number is not greater than 0) but the above statement will execute because it's true


# it the same case below
# number = 67
# if number < 0:
#     print("the number is negative") # this will not execute
# if number > 0:
#     print("the number is positive") # this will execute


# let's use ELIF statement
# number = 67
# if number < 0:
#     print("the number is negative") # this will not execute
# elif number > 0:
#     print("the number is positive") # this will execute


# let's define our own function in this case
# def checknum(num):
#     if num < 0:
#         print("Number is negative")
#     elif num > 0:
#         print("Number is positive")
# checknum(100)
# checknum(-40)
# checknum(10)


# An if statement that compares many numbers and checks the largest number
# def largest(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
# print(largest(40,10))
# print(largest(45,74))
# print(largest(58,36))
# print(largest(100,21))
# print(largest(0,46))


# To evaluate two or more statements like grading
# def mygrading(mark):
#     if mark > 90:
#         grading = "A"
#         return grading
#     elif (mark >= 80) and (mark < 90):
#         grading = "B"
#         return grading
#     elif (mark >=70) and (mark < 80):
#         grading = "C"
#         return grading
#     elif (mark >= 60) and (mark < 70):
#         grading = "D"
#         return grading
#     else:
#         grading = "E"
#         return grading

# print(mygrading(80))
# print(mygrading(45))
# print(mygrading(68))
# print(mygrading(100))
# print(mygrading(85))
# print(mygrading(67))
# print(mygrading(95))
# print(mygrading(24))
# print(mygrading(37))
# print(mygrading(97))


# Repeat the above with print function instead or return
# def formfour(mark):
#     if mark > 90:
#         grading = "A"
#         print(grading)
#     elif (mark >= 80) and (mark < 90):
#         grading = "B"
#         print(grading)
#     elif (mark >= 70) and (mark < 80):
#         grading = "C"
#         print(grading)
#     elif (mark >= 60) and (mark < 70):
#         grading = "D"
#         print(grading)
#     else:
#         grading = "E"
#         print(grading)

# formfour(40)
# formfour(98)
# formfour(73)
# formfour(56)
# formfour(86)
# formfour(65)