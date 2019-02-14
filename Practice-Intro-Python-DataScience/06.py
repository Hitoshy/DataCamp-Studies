import numpy as np 

store	= np.array([9,0,9,8])
cost	= np.array([60,88,87,86])
np_cols	= np.column_stack((store, cost))
print(np_cols)