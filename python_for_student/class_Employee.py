#class_Employee.py
class Employee:
  def __init__(self, 이름, 전화번호, 연봉):
     self.name = 이름;  self.tel = 전화번호;  self.pay = 연봉    
  def set_pay(self, 연봉):
     self.pay = 연봉
class Developer(Employee):
  def __init__(self, 이름, 전화번호, 연봉, 전공):
     Employee.__init__(self, 이름, 전화번호, 연봉) 
     self.major = 전공
class Manager(Employee):
  def __init__(self, 이름, 전화번호, 연봉, employees=[]):
     Employee.__init__(self, 이름, 전화번호, 연봉) 
     self.team = employees
  def add_emp(self, employees):
     if len(self.team) < 1: self.team.extend(employees)
     else:
       for emp in employees:  self.team.append(emp) 
  def subtract_emp(self, employees):
     for emp in employees:
        if emp in self.team:  self.team.remove(emp)
  def show_team(self):
     emp_names = [] 
     for emp in self.team:  emp_names.append(em)  
