#3. Write a program that has a class person storing name and date of birth of a person. The program should subtract the DOB from today's date to find out whether a person is eligible to vote or not.
import datetime
class person():
    def __init__(self, name, dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if age>=18:
            print(self.name, " , You are eligible to vote.")
        else:
            print(self.name, " , You should be at least 18 years to vote.") 
p=person("Anvitha", datetime.date(2001, 10, 20))
p.check()
