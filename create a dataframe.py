# Python program to create a dataframe containingcolumns name, age and percentage. Add 10 rows to the dataframe. View the dataframe 

import pandas as pd
import numpy as np
# Pass a 2D numpy array - each row is the corresponding row in the dataframe
data={'Name':['Abs','Tom','Joe','Mike','Sam','Vk','Rohit','Luke','Sena','Kia'],
'age':[21,20,18,24,19,19,28,32,24,25],
'percentage':[98,97,70,88,97,64,91,91,93,75]
}
# pass column names in the columns parameter of the constructor
df = pd.DataFrame(data)
df