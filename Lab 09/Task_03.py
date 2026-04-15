disease_model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'), ('Disease', 'Cough'), 
    ('Disease', 'Fatigue'), ('Disease', 'Chills')
])
cpd_dis = TabularCPD('Disease', 2, [[0.3], [0.7]]) 
cpd_fever = TabularCPD('Fever', 2, [[0.9, 0.5], [0.1, 0.5]], evidence=['Disease'], evidence_card=[2])
cpd_cough = TabularCPD('Cough', 2, [[0.8, 0.6], [0.2, 0.4]], evidence=['Disease'], evidence_card=[2])
cpd_fatigue = TabularCPD('Fatigue', 2, [[0.7, 0.3], [0.3, 0.7]], evidence=['Disease'], evidence_card=[2])
cpd_chills = TabularCPD('Chills', 2, [[0.6, 0.4], [0.4, 0.6]], evidence=['Disease'], evidence_card=[2])

disease_model.add_cpds(cpd_dis, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
d_infer = VariableElimination(disease_model)

print(d_infer.query(['Disease'], evidence={'Fever': 0, 'Cough': 0}))

print(d_infer.query(['Disease'], evidence={'Fever': 0, 'Cough': 0, 'Chills': 0}))

print(d_infer.query(['Fatigue'], evidence={'Disease': 0}))
