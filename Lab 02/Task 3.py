from re import S
class Student_Result:
  def __init__(self,student_id,name,marks):
    self.student_id=student_id
    self.name=name
    self.__marks=marks
  def display_info(self):
    print(f"Student ID: {self.student_id}") 
    print(f"Name: {self.name}")
    print(f"Marks: {self.__marks}")
  def get_marks(self):
    return self.__marks
  def set_marks(self,marks):
    self.__marks=marks
  def Calculate_grade(self):
    marks=self.get_marks()
    if marks>=90:
      return 'A'
    elif marks>=80:
      return 'B'
    elif marks>=70:
      return 'C'
    elif marks>=60: 
      return 'D'
    else:
      return 'F'

s1=Student_Result("S001","Hasnain",85)
s1.display_info()
grade=s1.Calculate_grade()
print(f"Grade: {grade}")
print("======================================")
s2=Student_Result("S002","Jawad",75)
s2.display_info()
grade=s2.Calculate_grade()
print(f"Grade: {grade}")
