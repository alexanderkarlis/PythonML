import numpy as np 
import pandas as pd 
import os

if True:
	try:
		data = 'data/'
		bcdata = os.listdir(data)
		print('Data found locally.')
	except:
		link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data'
		bcdata = pd.read_csv(link, header=None)
		print('Data acquired from remote repo {}'.format(link))    
 
bcdata.columns = ['Class', 'Age', 'Menopause', 'Tumor-Size','Inv-nodes',
 'Node-caps', 'Deg-malig', 'Breast', 'Breast-quad', 'Irradiant']
bcvals = bcdata.values
print(bcdata)

#grabbing the class labels (y), and Age & Tumor Size (X)

y = np.array(bcvals[:,0])
X = bcvals[:, [1, 3]] 

print('Class Labels:', np.unique(y))