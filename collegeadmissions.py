import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

# number of iterations
n = 8

# starting point for mu1 and mu2
mu1 = [[-130, 30]]
mu2 = [[-75, 45]]

# get our data
df = pd.read_excel (r'IPEDS_data.xlsx')

data = pd.DataFrame(df,columns=["Longitude location of institution","Latitude location of institution"])

# make the data a tuple of values
datapoints = data.values.tolist()

for x in range(n):
    # start with fresh lists of data
    sig1 = []
    sig2 = []
    mu1_n = mu1[x]
    mu2_n = mu2[x]
    # iterate over our datapoints
    for p in datapoints:
        # math formula to find if each p is nearer to p1 or p2
        # sqrt(dx^2+dy^2)
        d1 = math.sqrt((mu1_n[0]-p[0])**2+(mu1_n[1]-p[1])**2)
        d2 = math.sqrt((mu2_n[0]-p[0])**2+(mu2_n[1]-p[1])**2)
        if d1 < d2:
            sig1.append(p)
        else:
            sig2.append(p)
    
    sig1x = [x[0] for x in sig1]
    sig1y = [x[1] for x in sig1]
    
    sig2x = [x[0] for x in sig2]
    sig2y = [x[1] for x in sig2]
    
    # find average of data points
    mu1_i = [np.mean(sig1x), np.mean(sig1y)]
    mu2_i = [np.mean(sig2x), np.mean(sig2y)] 
    # add the average to the list of mu for plotting
    mu1.append(mu1_i)
    mu2.append(mu2_i)
    
mu1x = [x[0] for x in mu1]
mu1y = [x[1] for x in mu1]

mu2x = [x[0] for x in mu2]
mu2y = [x[1] for x in mu2]

plt.figure()

# plt.scatter(data.drop("Latitude location of institution", axis=1), data.drop("Longitude location of institution", axis=1), color='black',alpha=0.2,s=10)
plt.scatter(sig1x,sig1y,color="red",alpha=.4,s=4)
plt.scatter(sig2x,sig2y,color="blue",alpha=.4,s=4)
plt.scatter(mu1x,mu1y,color="violet",s=50)
plt.scatter(mu2x,mu2y,color="green",s=50)


plt.show