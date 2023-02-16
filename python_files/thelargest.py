largest = -1
print("Before", largest)
for the_num in [8, 41, 50, 42, 75, 12, 100] :
    if the_num > largest :
        largest = the_num
    print(largest, the_num)
print("After", largest)