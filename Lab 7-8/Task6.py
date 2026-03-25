from ortools.sat.python import cp_model

model=cp_model.CpModel()
x=model.NewIntVar(0,20,'x')
y=model.NewIntVar(0,20,'y')
z=model.NewIntVar(0,20,'z')
model.Add(x+2*y+z<=20)
model.Add(3*x+y<=18)
model.maximize(4*x+2*y+z)
solver=cp_model.CpSolver()
status=solver.solve(model)
if status == cp_model.OPTIMAL :
    print(f"Optimal Value: {solver.objective_value}")
    print(f"x = {solver.value(x)}")
    print(f"y = {solver.value(y)}")
    print(f"z = {solver.value(z)}")
else:
  print("No solution found.")
