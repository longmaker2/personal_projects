# def name():
#     print(input("Enter your name: "))

# name()



# def firstname (name):
#     print(name)

# firstname("Long")



# def myfunc(t1,t2,t3,t4):
#     print(t1+t2+t3+t4)

# myfunc(2,3,4,5)



# def tot(*args):
#     print(sum(args))

# tot(100,200,400,500,600,700,800,900)



# def give_details(name, age):
#     print(f"My name is: {name}")
#     print(f"I am {age} years old")

# give_details("Long Maker", 24)



# def area(side):
#     print(f"Area of a squre with a side of {side} units is {side * side}")

# area(2)
# area(4)
# area(6)


def total(*args):
    return sum(args)

print(f"The sum of all my args is {total(100,100,100,100,100)}")
