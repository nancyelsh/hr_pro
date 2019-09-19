from datetime import date
today = date.today()

class Employee:
  def __init__(self, name, age, salary, employment_date):
    self.name = name
    self.age = age
    self.salary = salary
    # Enter date in (year,month,date) format
    self.employment_date = employment_date
    #year,month,day = employment_date(',')
  def get_working_years(self):
    return today.year - self.employment_date
    #return today.year - year - ((today.month, today.day) < (month, day))
  def __str__(self):
    return "Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working years: {}".format(self.get_working_years(), self = self)

class Manager:
  def __init__(self, name, age, salary, employment_date, bonus_percentage):
    self.name = name
    self.age = age
    self.salary = salary
    # Enter date in (year,month,date) format
    self.employment_date = employment_date
    #year,month,day = employment_date(',')
    self.bonus_percentage = bonus_percentage
  def get_working_years(self):
    return today.year - self.employment_date
    #return today.year - year - ((today.month, today.day) < (month, day))
  def get_bonus(self):
    return self.bonus_percentage*self.salary
  def __str__(self):
    return "Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working years: {}, Bonus: {}".format(self.get_working_years(), self.get_bonus(), self = self)
  
employees = []
managers = []
  
print("""Welcome to HR Pro 2019
  Options:
    1. Show Employees
    2. Show Managers
    3. Add an Employee
    4. Add a Manager
    5. Exit\n""")
option = input("What would you like to do? ")
while option != '5':
  if option == '1':
    print("-----------------")
    print("Employees\n")
    for employee in employees:
      print(employee)
    print("-----------------")
    print("""Welcome to HR Pro 2019
      Options:
        1. Show Employees
        2. Show Managers
        3. Add an Employee
        4. Add a Manager
        5. Exit\n""")
    option = input("What would you like to do? ")
  elif option == '2':
    print("-----------------")
    print("Managers\n")
    for manager in managers:
      print(manager)
    print("-----------------")
    print("""Welcome to HR Pro 2019
      Options:
        1. Show Employees
        2. Show Managers
        3. Add an Employee
        4. Add a Manager
        5. Exit\n""")
    option = input("What would you like to do? ")
  elif option == '3':
    print("-----------------")
    name = input("Name: ")
    age = input("Age: ")
    salary = input("Salary: ")
    employment_date = input("Employment year: ")
    employees.append(Employee(name, int(age), int(salary), int(employment_date)))
#    employees.append(new_employee)
    print("Employee added successfully")
    print("-----------------")
    print("""Welcome to HR Pro 2019
      Options:
        1. Show Employees
        2. Show Managers
        3. Add an Employee
        4. Add a Manager
        5. Exit\n""")
    option = input("What would you like to do? ")
  elif option == '4':
    print("-----------------")
    name = input("Name: ")
    age = input("Age: ")
    salary = input("Salary: ")
    employment_date = input("Employment year: ")
    bonus = input("Bonus percentage: ")
    managers.append(Manager(name, int(age), int(salary), int(employment_date), float(bonus)))
#    managers.append(new_manager)
    print("Manager added successfully")
    print("-----------------")
    print("""Welcome to HR Pro 2019
      Options:
        1. Show Employees
        2. Show Managers
        3. Add an Employee
        4. Add a Manager
        5. Exit\n""")
    option = input("What would you like to do? ")
#    new_employee = Employee(input("Add an employee in the format (name, age, salary, employment date),\nex: ('Nancy', 25, 600, (2019,2,5))"))
#      employees.append(new_employee)
#  elif option == '4':
#    new_manager = Manager(input("Add a manager in the format (name, age, salary, bonus percentage, employment date), \nex: ('Nancy', 25, 600, 25, (2019,2,5))"))
#      managers.append(new_manager)
