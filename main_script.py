import opensim as osim
import sys

model_filename = 'gait9dof18musc_Thelen_BigSpheres_20160914.osim'

model = osim.Model(model_filename)

state = model.initSystem()
model.setUseVisualizer(True)

init_state = [0.0, 2.0, 3.5, 0.0, 1.5, 0, 0, 0, 0, 0]

editableCoordSet = model.updCoordinateSet()

for i in range(0,editableCoordSet.getSize()):
	editableCoordSet.get(i).setValue(state, init_state[i])

manager = osim.Manager(model)
finalTime = 1
manager.setIntegratorAccuracy(1e-2) # make it larger 
manager.initialize(state)
manager.semi_explicit_euler(finalTime)
integrator.setFixedStepSize(dt)

statesDegrees = manager.getStateStorage()
states_table = manager.getStatesTable()
osim.STOFileAdapter.write(states_table, "forwardSimulation.sto")


# What is the largest integration accuracy you can use without encountering an integration error?
# according to the results, the number of iterations required to achieve the desired accuracy decreases with higher integration accuracy. The largest integration accuracy that can be used without encountering an integration error is 1e-2.

# Does your simulation produce a different result at the largest integration accuracy compared to 1e-10?
# If yes, which result is more accurate?
# Yes, the simulation produces different results at the largest integration accuracy compared to 1e-10. The result obtained with an integration accuracy of 1e-10 is more accurate than 1e-2


# 3. Can you change the integrator used to be a SemiExplicitEuler2Integrator (search online, the OpenSim API) 
# and then set the step size dt as follow: 
# integrator.setFixedStepSize(dt))