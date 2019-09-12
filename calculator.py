first_no = input("Enter the first number: ")
second_no = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

#if type("first_no") != int or float:
#  print("First Number is invalid")
#if type("second_no") != int or float:
#  print("Second Number is invalid")

try:
   val1 = int(first_no)
except ValueError:
   print("That's not an int!")

try:
   val2 = int(second_no)
except ValueError:
   print("That's not an int!")

if operation == '+':
  print("The answer is {}".format((int(first_no) + int(second_no))))
elif operation == '-':
  print("The answer is {}".format((int(first_no) - int(second_no))))
elif operation == '*':
  print("The answer is {}".format((int(first_no) * int(second_no))))
elif operation == '/':
  print("The answer is {}".format((int(first_no) / int(second_no))))
else:
  print("The operation is invalid")
