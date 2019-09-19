skills = ['Python', 'C++', 'Javascript', 'Juggling', 'Running', 'Eating']
cv = {}
print("Welcome to the special recruitment program, please answer the following questions: ")
cv['name'] = input("What's your name? ")
cv['age'] = input("How old are you? ")
cv['experience'] = input("How many years of experience do you have? ")
cv['skills'] = []
print("""Skills:
1- Python
2- C++
3- Javascript
4- Juggling
5- Running
6- Eating""")
cv['skills'].append(input("Choose a skill from above by entering its number: "))
cv['skills'].append(input("Choose another skill from above by entering its number: "))
if int(cv['age']) > 25 and int(cv['age']) < 40 and int(cv['experience']) > 3 and '1' in cv["skills"]:
    print("You have been accepted, {}!".format(cv['name']))
else:
    print("We're sorry, {}.".format(cv['name']))
