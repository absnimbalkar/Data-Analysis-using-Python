import numpy as np
import pandas as pd
df=pd.read_csv('D:\Data.csv')
df

# Describing the dataset , Shape of the dataset & Display first 3 rows from dataset
df.describe()
df.describe()
df.head(3)
df.info()
df.dtypes
df.size()
df.columns()