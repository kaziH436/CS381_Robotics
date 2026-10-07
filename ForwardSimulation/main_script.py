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
# finalTime = 1
finalTime = 5 
manager.initialize(state)
manager.integrate(finalTime)

statesDegrees = manager.getStateStorage()
statesDegrees.printToFile("forwardSimulation.sto", "w")
