import numpy as np 
import pandas as pd 

bcdata = pd.read_csv('breast-data.csv', header=None)    
bcdata.columns = ['Class', 'Age', 'Menopause', 'Tumor-Size','Inv-nodes',
 'Node-caps', 'Deg-malig', 'Breast', 'Breast-quad', 'Irradiant']
bcvals = bcdata.values
print(bcdata)

#grabbing the class labels (y), and Age & Tumor Size (X)

y = np.array(bcvals[:,0])
X = bcvals[:, [1, 3]] 

print('Class Labels:', np.unique(y))