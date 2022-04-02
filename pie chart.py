# Program for pie chart

import matplotlib.pyplot as plt
import numpy as np
subject = ['Operating System','Java','Web Technology','Python','Data Science','Block Chain']
Marks = [24,55,12,41,36,17]
plt.pie(Marks, labels = subject)
plt.show()
plt.barh(subject,Marks,color="red")
plt.show()