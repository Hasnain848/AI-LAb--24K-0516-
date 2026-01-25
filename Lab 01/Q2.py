n = int(input("Enter a number: "))
i=2
count=0
print("Even numbers: ",end =" ")
while i<=n:
  if i % 2 == 0:
    count+=1
    print(i,end =" ")
  i+=1
print()
print("Total even numbers",count)
