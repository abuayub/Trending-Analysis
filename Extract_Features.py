import numpy as np

data = np.loadtxt("Data/pagecounts-20110101-000000",dtype='string', delimiter=" ")
print data.shape
print data[0:10,2]
np.savetxt("foo1.csv", data[0:1000,2].astype(int ), delimiter=",")