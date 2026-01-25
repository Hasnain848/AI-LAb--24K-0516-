my_dict = {}
for i in range(3):
  name=input("Enter name: ")
  marks=int(input("Enter marks: "))
  my_dict[name] = marks
print("\nStudent Records")
for name ,marks in my_dict.items():
  print(name,":",marks)
