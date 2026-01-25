def addnumber(a,b):
  return a+b
def subtract(a,b):
  return a-b
while(1):
  print("1. Add Two Numbers.")
  print("2. Subtract Two Numbers.")
  print("3. Exit.")
  choice =int(input("Enter your choice: "))
  if choice == 1:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result: ",addnumber(a,b))
  elif choice == 2:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Result: ",subtract(a,b))
  elif choice == 3:
    break
  else:
    print("Invalid Choice")

    