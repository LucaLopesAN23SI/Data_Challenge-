# This is a sample Python script.
from ftplib import print_line

import pandas as pd
import numpy as np
import seaborn as sns


#finding out the resolution rate by call type
ModifiedDataFrame = pd.read_csv('team17_callcenter_modified.csv')
resolved = ModifiedDataFrame.groupby('call_type')['resolved'].value_counts(normalize=True)
print_line(resolved)


#Finding the which time of day is the longest
groupByDay = ModifiedDataFrame.groupby('time_of_day')['duration_minutes'].mean()
print_line(groupByDay)

#finding the percentage of resolved high priority calls
highPriority = ModifiedDataFrame.groupby('priority')['resolved'].value_counts(normalize=True)*100
print_line(highPriority)