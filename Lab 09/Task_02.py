from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('I', 'G'), ('S', 'G'), ('D', 'G'), ('G', 'P')])
cpd_i = TabularCPD('I', 2, [[0.7], [0.3]]) # High, Low
cpd_s = TabularCPD('S', 2, [[0.6], [0.4]]) # Sufficient, Insufficient
cpd_d = TabularCPD('D', 2, [[0.4], [0.6]]) # Hard, Easy

# P(G | I, S, D) - 2x2x2=8 combinations for parents
cpd_g = TabularCPD('G', 3, [
    [0.9, 0.7, 0.8, 0.4, 0.7, 0.3, 0.5, 0.1], # Grade A
    [0.08, 0.2, 0.15, 0.4, 0.2, 0.4, 0.3, 0.4], # Grade B
    [0.02, 0.1, 0.05, 0.2, 0.1, 0.3, 0.2, 0.5]  # Grade C
], evidence=['I', 'S', 'D'], evidence_card=[2, 2, 2])

# P(P | G)
cpd_p = TabularCPD('P', 2, [
    [0.95, 0.80, 0.50], # Pass = Yes
    [0.05, 0.20, 0.50]  # Pass = No
], evidence=['G'], evidence_card=[3])

model.add_cpds(cpd_i, cpd_s, cpd_d, cpd_g, cpd_p)
infer = VariableElimination(model)
print("P(Pass | Study=Sufficient, Difficulty=Hard):")
print(infer.query(['P'], evidence={'S': 0, 'D': 0}))

print("\nP(Intelligence | Pass=Yes):")
print(infer.query(['I'], evidence={'P': 0}))
