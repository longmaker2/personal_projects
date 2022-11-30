# number = 0
# while number < 6:
#     print(number)
#     number += 1         # this increment execute adding 1 as long as the number is less than 6. Meaning that this number will start printing from 0 to 6

# number = 0
# while number < 6:
#     print(number)
#     number = number + 1   # this is the same as (number += number + 1)



# GUESS GAME
# correct_number = 100

# guess = 0
# while guess != correct_number:
#     guess = int(input("Enter your guess: "))
#     if guess == correct_number:
#         print("You win!!!")
#     print ("Continue")    # This will still print continue!

# correct_number = 100

# guess = 0
# while guess != correct_number:
#     guess = int(input("Enter your guess: "))
#     if guess == correct_number:
#         print("You win!!!")
#     else:
#         print ("Continue")      # In this case continue will not be printed because one of the conditions is met

# Let's use break statement below
# correct_number = 100

# guess = 0
# while guess != correct_number:
#     guess = int(input("Enter your guess: "))
#     if guess == correct_number:
#         print("You win!!!")
#         break
#     print ("Continue")          # The break statement will break the execution and continue will not be print after the condition is met

# correctnumber = 456
# guess = None                      # You can also use None reserve word instead of zero here
# while guess != correctnumber:
#     guess = int(input("Enter your guess number here: "))
#     if guess == correctnumber:
#         print("Wow you won!!!")
#     else:
#         print("Try again")