class Employee():
    def name(self, a):
        print(a)
class Salary():
    def Salary(self, a):
        print(a)
class Designation(Employee, Salary):
    def design(self):
        print("Designation Test Engineer")

call = Designation()
call.name("Hussain")
call.Salary("10000")
call.design()