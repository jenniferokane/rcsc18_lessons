% matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np 

def circle_bound(x):
    y = np.sqrt(1-x**2)
    #print(y)
    return y

def make_pi(tot_points):
	circ_points=0


	for i in range(tot_points):

		point_x = np.random.uniform(0,1)
		point_y = np.random.uniform(0,1)
		
		if circle_bound(point_x) >= point_y:
			circ_points = circ_points+1
			
		pi = 4 * (circ_points/tot_points)

	return pi