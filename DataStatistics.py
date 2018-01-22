from DataExploration import dur,ts2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels import robust
s = pd.Series(dur)
descriptive_statistics = s.describe()
print('------Descriptive Statistics-----')
print(descriptive_statistics)


#Anomaly detection using Robust Statistics
med = np.median(dur)
mean = np.mean(dur)
max = np.max(dur)
mad = robust.mad(dur)
anomaly = []
for a in dur:
    robust_scores= (a - med)/mad
    if (robust_scores > 2.5):
        anomaly.append(a)
#data.describe()

print('\n# of Anolmaly',np.shape(anomaly)[0],'/944')
