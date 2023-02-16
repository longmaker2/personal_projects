largest = None
smallest = None
while True:
 num = input("Enter a number:")
 try:
  if num == 'done':
   print("Maximum is",largest)
   print("Minimum is",smallest)
   break
  num = int(num)
  if largest is None:
   largest = num
  if smallest is None:
   smallest = num
  if largest < num:
   largest = num
  if smallest > num:
   smallest = num
 except:
  print("Invalid input")