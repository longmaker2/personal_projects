isMale = True
# print(not isMale)

isAdult = False
# print(not isAdult)

# NOT True = False
# NOT False = True



# OR
# True or False = True (It's always true, as long as it's true on one side)
# False or True = True (the same as the above)
# False or False = False (It's always false if both sides are false)
# True or True = True (is the same as the above)

# for example
# print(isMale or isAdult) # This will print True because of both statements is true



# AND
# True and True = True (this will print true if both sides are true)
# True and False = False (this will will print false if any of the sides is false)
# False and True = False (is the same as the above)
# False and False = False (this will print false because both sides are false)

# for example
# print(isMale and isAdult) # this will print false because one of the sides is false. You can achieve true if both sides are true
print(isMale and not isAdult) # this will print true because the second statement in the boolean variable is being opposed to true