#first_no = input("Enter the first number: ")
#second_no = input("Enter the second number: ")
#operation = input("Choose the operation (+, -, *, /): ")

while True:
    try:
        first_no = int(input("Enter the first number: "))
        second_no = int(input("Enter the second number: "))
    except ValueError:
        print("Numbers were invalid")
        continue
    else:   
        break

operation = input("Choose the operation (+, -, *, /): ")

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
