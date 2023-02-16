# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates
# put a coma to separate keys in the dictionary
# use double or single quotes when printing any key in the dictionary and also square bracket after the variable

# person = {
#     "name" : "Long Maker-Gutajah",
#     "age" : 24,
#     "country" : "South Sudan",
#     "Father's name" : "Maker Long"}
# print(person["name"])
# print(person["age"])
# print(person["country"])
# print(person["Father's name"])



# dictionaries that has keys that are in number form
# here we are able to add dictionaries with their keys
# with dictionaries we are able to store any data type

# mydict = {

# }
# mydict[1] = "Good work muony"
# mydict["country"] = "Kenya"
# mydict["age"] = 24
# mydict["name"] = "Long"
# mydict["price"] = 2000

# print(mydict["country"])
# print(mydict[1])
# print(mydict["name"])

# here the user is prompted to add their details

# mydict = {

# }
# mydict["name"] = input("Enter your name: ")
# mydict["country"] = input("Enter your country: ")
# mydict["age"] = int(input("Enter your age: "))

# print(mydict)



# A dictionary with a list of collection
# In the below code we use [] square brackets because of the list of students within the dictionary separated with comas

# students = {
#     "collection" : [
#         {
#             "name" : "Long",
#             "age" : 24
#         },
#         {
#             "name" : "Ruth",
#             "age" : 20
#         }
#     ],
#     "classes" : [
#         {
#             "f1" : "form one",
#             "f2" : "form two"
#         },
#         {
#             "f3" : "form three",
#             "f4" : "form four"
#         }
#     ]
# }

# print(students["collection"][1]["age"])
# print(students["classes"][0]["f2"])


# listit = {
#     "collection" : [
#         {
#             "item" : "oil",
#             "daugher" : "Joy",
#             "son" : "Daniel"
#         },
#         {
#             "name" : "Long",
#             "age" : input("Enter your age: ")
#         }
#     ]
# }

# print(listit["collection"][1]["age"])


mycollect = {
    "teams" : [
        {
            "team1" : "Golden Factory",
            "team2" : "Jupiter",
            "team3" : "City Boys"
        },
        {
            "one" : "Giroud",
            "two": "Paulo",
            "three" : "Wrong"
        }
    ],
    "leagues" : [
        {
            "league1" : "EPL",
            "league2" : "La Liga",
            "league3" : "Seria A"
        }
    ]
}

print(mycollect["teams"][0]["team3"])