import cma
import opensim as osim
import sys
import math
import numpy as np

KNOTS = 3
solution_file = 'sol.txt'

# You will see lines with “TODO” indicating what could be changed in the file for the character to stay in balance (and not fall on the floor).  How would the simulation look differently if you changed the number of iterations (maxiter) from 1 to 20? 
# What cost function term could you add for the right toe to get as high as possible? Submit your code and a short write-up. 


def simfunc(params, viz=False):
		
	model_filename = 'gait9dof18musc_Thelen_BigSpheres_20160914.osim'

	model = osim.Model(model_filename)
	init_state = [0, 2.0, 1.02, 0, 0, 0, 0, 0, 0, 0]
	stepsize = 0.005
	nbr_timesteps = 200

	state = model.initSystem()
	muscleController = osim.PrescribedController()
	muscleSet = model.getMuscles()
	nbr_muscles = muscleSet.getSize()

	#state = model.initSystem()
	editableCoordSet = model.updCoordinateSet()

	for i in range(0,editableCoordSet.getSize()-1):
		editableCoordSet.get(i).setValue(state, init_state[i])

	manager = osim.Manager(model)
	manager.initialize(state)

	f = 0

	total_time = stepsize * nbr_timesteps

	for i in range(0,nbr_timesteps+1):
		t = (i+1) * stepsize
		state = manager.integrate(t)
		phase = min(math.floor((t*KNOTS)/total_time),KNOTS-1)

		for j in range(0,nbr_muscles):
			muscleSet.get(j).setActivation(state, params[phase*nbr_muscles+j])

		model.realizeDynamics(state)
		com = model.calcMassCenterPosition(state)
		
		# TODO: change one thing in the line below to encourage the character to stay upright.
		# f = f + com.get(0)
		f = f + com.get(1) 

		# The cost function will be to get the right heel as high as possible at the very end of the simulation
		# what cost function term could you add after the line below:
		heel_r = model.getBodySet().get("calcn_r").getTransformInGround(state).p() 

		# also need to make the right toe as high as possible
		toes_r = model.getBodySet().get("toes_r").getTransformInGround(state).p() 
		
		if i == nbr_timesteps:
			f = f + heel_r.get(1) * 9000
			f = f + toes_r.get(1) * 9000
		
	
	if viz:
		statesDegrees = manager.getStateStorage()
		states_table = manager.getStatesTable()
		osim.STOFileAdapter.write(states_table, "forwardSimulation.sto")
		#statesDegrees.printToFile("optSimulation.sto", "w");

	# goal is to minimize f since its the cost fucntion and to do this, it minimizes by moving the x direction
	f = -1 * f 
	print(f)
	return f


def parallel_func():
	import multiprocessing as mp
	# TODO: you should try changing maxiter and popsize
	# es = cma.CMAEvolutionStrategy(KNOTS*18 * [0], 0.3, {'maxiter':1, 'popsize':8})
	# increasing the maxiter makes better results
	es = cma.CMAEvolutionStrategy(KNOTS*18 * [0], 0.3, {'maxiter':50, 'popsize':8})
	pool = mp.Pool(es.popsize)
	while not es.stop():
		X = es.ask()
		f_values = pool.map_async(simfunc, X).get()
		es.tell(X, f_values)
	simfunc(es.result[0], True)
	np.savetxt(solution_file, es.result[0])


def replay_solution():
	sol = np.loadtxt(solution_file)
	simfunc(sol, True)

if __name__ == '__main__':	
	parallel_func()
	#replay_solution()



