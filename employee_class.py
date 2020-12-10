#2. Write a program with class Employee that keeps a track of the number of employees in an organization and also stores their name, designation and salary details.
class Employee(object):
    count=0
    def __init__(self, name, desg, salary):
        self.name = name
        self.desg = desg
        self.salary = salary
        Employee.count+=1
    def getdesg(self):
        return self.desg
    def getsalary(self):
        return self.salary
    def __str__(self):
        return self.name + ' : ' + str(self.getdesg()) +' -  '+  str(self.getsalary())
   
def empl(rec, name, desg, salary):
    rec.append(Employee(name, desg, salary))
    return rec

Record = []
x = 'y'
while x == 'y':
    name = input('Enter the name of the employee: ')
    desg = input('Enter the designation: ')
    salary = input('Salary: ')
    Record = empl(Record, name, desg, salary)
    x = input('Add Another Employee? y/n: ')
n = 1
for el in Record:
    print(n,'. ', el)
    n = n + 1
print("Total no. of employees: ",Employee.count)
