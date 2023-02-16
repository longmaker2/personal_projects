# list is a collection of items
# a list can store items of the same data type or different types
# we use square brackets when writing a list in python
# we can access items in the list using indices and indices starts from 0, meaning the item in a list can be accessed using index 0

# names = ["Long", "Ruth", "Daniel", "David", "Flore,", "Lomotey"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[-1])        # We can also use negative numbers to access each item in the list from the last item as index -1

# things = ["Mach", "Garang", "Achol", "Adit",7,8,[1,2,3,4]]  # Mixed data types in a list. Also, a list that's in another list is called a nested list.

# print(things[0])
# print(things[1])
# print(things[2])
# print(things[-4])
# print(things[5])



# How to add items to a list

# names = []      # use empty [] because the user is going to add items to the list stored in names
# for i in range(0,6):        # here we use for loop to specify the last entry of names and end the loop instead of making it run forever
#     addname = input("Enter a name: ")
#     names.append(addname)       # this line means that anything that the user will enter will be added to the list stored in the variable namesuj n
#     print(names)

# if you just want to add an item to an existing list
# theseitems = ["one", "two", "three"]
# theseitems.append("four")
# print(theseitems)



# How to remove items from a list using del function
# rm_items = ["Adit","Achol", "Akeer", "Ruth", "Flore"]
# del rm_items[-1]        # items to be deleted are specified using their index numbers
# del rm_items[2]
# print(rm_items)



# Let's create a list that contains another list (Nested list)
# my2lists = [["tok","rou", "diak"], ["one", "two", "three"]]
# print(my2lists[0][-1])
# print(my2lists[1][-2])


# HOW TO SORT ITEMS IN A LIST
# a list of sorted alphabets
# friends = ["Long", "Ruth", "Daniel", "David", "Flore,", "Lomotey"]
# print(sorted(friends))

# A list of sorted numbers
# sortednumbers = [54,87,12,0,6,1,3,5,2,100]
# print(sorted(sortednumbers))

# A slicing list print from a specified index in a list to another specified index in the same list
# numbers = [54,87,12,0,6,1,3,5,2,100]
# print(numbers[0:5])
# print(numbers[2:7])         # In slicing list we use full collon: to specify indices to be printed