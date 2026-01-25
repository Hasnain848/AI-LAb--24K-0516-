def calculate_average(my_list):
  return sum(my_list)/len(my_list)
marks = []
for i in range(3):
  marks.append(int(input("Enter marks: ")))
print("Average marks: ",calculate_average(marks))