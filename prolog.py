# import necessary libraries 
! pip install scikit-fuzzy
import skfuzzy as fuzzy
from skfuzzy import control
import numpy as np 

# create universes
service_range = np.arange(0, 100, 1)
food_range = np.arange(0, 100, 1)
tips_range = np.arange(0, 25, 1)

service = control.Antecedent(service_range, 'service')
food = control.Antecedent(food_range, 'food')
tips = control.Consequent(tips_range, 'tips')

# apply memebrship functions
service.automf(3)
food.automf(3)
tips.automf(3)

# view them
service.view()
food.view()
tips.view()

# create your rulebase including at least 4 rules
rule_1 = control.Rule(service['poor'] & food['poor'], tips['poor'])
rule_2 = control.Rule(service['average'] & food['average'], tips['average'])
rule_3 = control.Rule(service['good'] & food['good'], tips['good'])
rule_4 = control.Rule(service['average'] & food['poor'], tips['average'])
rule_5 = control.Rule(service['poor'] & food['average'], tips['poor'])
rule_6 = control.Rule(service['good'] & food['poor'], tips['average'])
rule_7 = control.Rule(service['poor'] & food['good'], tips['average'])

# create a control system
control_system = control.ControlSystem([rule_1,
                                        rule_2,
                                        rule_3,
                                        rule_4,
                                        rule_5,
                                        rule_6,
                                        rule_7])
# create a simulation
simulation = control.ControlSystemSimulation(control_system)

# run the fuzzy machine
simulation.input['service'] = 10
simulation.input['food'] = 80
simulation.compute()
# show the result
tips.view(sim = simulation)
print(simulation.output['tips'])
