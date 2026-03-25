class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
  def __init__(self,variable : list[cp_model.IntVar]):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variable = variable
    self.__sol_count=0
  def OnSolutionCallback(self) -> None:
      self.__sol_count+=1
      for v in self.__variable:
        print(f"{v}={self.value(v)}",end=" ")
      print()
  @property
  def solution_count(self):
    return self.__sol_count
def search_for_all_solutions_sample_sat():
  model=cp_model.CpModel()
  num_vals=4
  A=model.NewIntVar(0,num_vals-1,"A")
  B=model.NewIntVar(0,num_vals-1,"B")
  C=model.NewIntVar(0,num_vals-1,"C")
  model.Add(A!=B)
  model.Add(B!=C)
  model.Add(A+B<=4)
  solver=cp_model.CpSolver()
  solution_printer=VarArraySolutionPrinter([A,B,C])
  solver.parameters.enumerate_all_solutions=True
  status=solver.solve(model,solution_printer)

  print(f"Status = {solver.status_name(status)}")
  print(f"Number of solutions found: {solution_printer.solution_count}")

search_for_all_solutions_sample_sat()
