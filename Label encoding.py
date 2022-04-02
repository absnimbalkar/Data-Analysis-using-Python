#  Python program for Label encoding

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df.iloc[:,-1] = le.fit_transform(df.iloc[:,-1])
df