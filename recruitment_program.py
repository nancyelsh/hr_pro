skills = ['Python', 'C++', 'Javascript', 'Juggling', 'Running', 'Eating']
cv = {}

print("Welcome to the special recruitment program, please answer the following questions: ")
cv['name'] = input("What's your name?")
name = cv['name']
cv['age'] = input("How old are you?")
age = cv['age']
cv['experience'] = input("How many years of experience do you have?")
experience = cv['experience']
cv['skills'] = []

print("""Skills:
1- Python
2- C++
3- Javascript
4- Juggling
5- Running
6- Eating""")

cv['skills'][0].append(input("Choose a skill from above by entering its number: ")
#cv['skills']append(input("Choose another skill from above by entering its number: ")

"""if age > 25:
  if age < 40:
    if experience > 3:
      if 'Pythons' in skills:
        print("You have been accepted, name")
else:
  print("We're sorry, name")"""

while True:
  try:
   cv['age'] > 25
  except ValueError:
   break

  try:
   cv['age'] < 4
  except ValueError:
   break

  try:
   cv['experience'] > 3
  except ValueError:
   break

  try:
   'Pythons' in cv['skills']
   print("You have been accepted, cv['name']")
  except ValueError:
   break

print("We're sorry, name")
