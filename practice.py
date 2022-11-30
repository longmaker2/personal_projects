score = input("Enter Score: ")
inscore =  float(score)
outscore = 'Error'
if inscore >= 0.9:
	print("A")
elif inscore >=0.8:
	print("B")
elif inscore >=0.7:
	print("C")
elif inscore >= 0.6:
	print("D")
elif inscore < .6:
	print("F")
else:
	print("Out of Range")