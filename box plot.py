# Program for box plot

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
np.random.seed(23685752)
N_points = 50
n_bins = 20
x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(50) + 25
data = {'x': x, 'y' : y}
df = pd.DataFrame(data)
size = 50
import numpy as np
df.boxplot( column =['x'], grid = False)