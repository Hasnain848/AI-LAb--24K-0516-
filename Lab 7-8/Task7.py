from ortools.sat.python import cp_model

model = cp_model.CpModel()
queens = [model.new_int_var(0, 3, f'q{i}') for i in range(4)]

model.add_all_different(queens)

model.add_all_different(queens[i] + i for i in range(4))
model.add_all_different(queens[i] - i for i in range(4))

solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.OPTIMAL:
    for i in range(4):
        row = ['_'] * 4
        row[solver.value(queens[i])] = 'Q'
        print(' '.join(row))
