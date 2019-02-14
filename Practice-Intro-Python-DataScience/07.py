import numpy as np 

costs 		= np.column_stack(([1,1,3,3],[4,7,4,4]))
mean_costs	= np.mean(costs[:,1])
print(mean_costs) 