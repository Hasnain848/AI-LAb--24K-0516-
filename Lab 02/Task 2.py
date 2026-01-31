class Employee:
  def __init__(self,employee_id,name):
    self.employee_id=employee_id
    self.name=name
  def Calculate_salary(self):
    pass
  def display_info(self):
    print(f"Employee ID: {self.employee_id}")
    print(f"Name: {self.name}")
class FullTimeEmployee(Employee):
  def __init__(self,monthly_salary,employee_id,name):
    super().__init__(employee_id,name)
    self.monthly_salary=monthly_salary
  def Calculate_salary(self):
    return self.monthly_salary
class PartTimeEmployee(Employee):
  def __init__(self,hourly_rate,hours_worked,employee_id,name):
    super().__init__(employee_id,name)
    self.hourly_rate=hourly_rate
    self.hours_worked=hours_worked
  def Calculate_salary(self):
    return self.hourly_rate*self.hours_worked
fte=FullTimeEmployee(500000,"H001","Hasnain")
fte.display_info()
salary=fte.Calculate_salary()
print(f"Salary: {salary}")
print("======================================")
pte=PartTimeEmployee(1000,360,"J002","Jawad")
pte.display_info()
salary=pte.Calculate_salary()
print(f"Salary: {salary}")

