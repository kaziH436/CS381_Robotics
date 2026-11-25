import opensim as osim
import sys
import math
import numpy as np

model_filename = 'ue_torque.osim'

# Write Up
# Shoulder overshoots:** reduced derivative gain from 1 to 0.2 with proportional gain at 20
# Less damping in the movement

# Shoulder undershoot:* reduced proportional gain to 5 and increased derivative gain to 5
# More damping in the movement

# target faster:** Increased proportional gain to 50 and the derivative gain to 5
# The large proportional gain has a stronger correction to the target

# The proportional gain controls how strongly the controller responds to the difference between the current and target angles. 
# The derivative gain controls how strongly the controller responds to angular velocity

model = osim.Model(model_filename)
stepsize = 0.005
nbr_timesteps = 150

state = model.initSystem()
muscleController = osim.PrescribedController()
muscleSet = model.getMuscles()
torqueSet = model.getActuators()
nbr_muscles = muscleSet.getSize()

for j in range(torqueSet.getSize()):
	func = osim.Constant(1.0)
	muscleController.addActuator(torqueSet.get(j))
	actu = torqueSet.get(j)
	muscleController.prescribeControlForActuator(actu.getName(), func)
model.addController(muscleController)

#model.setUseVisualizer(True)

state = model.initSystem() 
coords = model.updCoordinateSet()

model.equilibrateMuscles(state)
manager = osim.Manager(model)
manager.initialize(state)

f = 0

total_time = stepsize * nbr_timesteps

com_i = model.calcMassCenterPosition(state)
max_com = -math.inf

for i in range(0,nbr_timesteps+1):
	t = state.getTime() + stepsize
	state = manager.integrate(t)
		
	brain = osim.PrescribedController.safeDownCast(model.getControllerSet().get(0))
	functionSet = brain.get_ControlFunctions()

	shoulder_elv = coords.get('shoulder_elv').getValue(state)
	shoulder_elv_v = coords.get('shoulder_elv').getSpeedValue(state)

	elbow_flexion = coords.get('elbow_flexion').getValue(state)
	elbow_flexion_v = coords.get('elbow_flexion').getSpeedValue(state)

	for j in range(functionSet.getSize()):
		func = osim.Constant.safeDownCast(functionSet.get(j))
		
		if j == 1:
			func.setValue(-20 * (shoulder_elv - 3.14159) - 5 * shoulder_elv_v)
		elif j == 3:
			func.setValue(-20 * (elbow_flexion - 0.0) - 1 * elbow_flexion_v) 


	model.realizeDynamics(state)
	com = model.calcMassCenterPosition(state)

states_table = manager.getStatesTable()
osim.STOFileAdapter.write(states_table, "PDcontrol.sto")
