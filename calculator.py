first_no = input("Enter the first number: ")
second_no = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

try:
   val1 = int(first_no)
   val2 = int(second_no)
except ValueError:
   print("Numbers were invalid")

if operation == '+':
  print("The answer is {}".format((int(first_no) + int(second_no))))
elif operation == '-':
  print("The answer is {}".format((int(first_no) - int(second_no))))
elif operation == '*':
  print("The answer is {}".format((int(first_no) * int(second_no))))
elif operation == '/':
  print("The answer is {}".format((int(first_no) / int(second_no))))
else:
  print("Operation is invalid")
