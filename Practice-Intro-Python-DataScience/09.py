import numpy as np 

store	= np.array(["X","X","Y","Y"])
cost	= np.array([6,8,3,8])
select_cost = cost[store == "Y"]
print(select_cost)