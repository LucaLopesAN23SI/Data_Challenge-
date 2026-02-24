# This is a sample Python script.
from ftplib import print_line

import pandas as pd
import numpy as np
import seaborn as sns

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings


varaible = pd.read_csv('team17_callcenter.csv')

#finding out the resolution rate by call type
resolved = varaible.groupby('call_type')['resolved'].value_counts(normalize=True)
print_line(resolved)


#Finding the which time of day is the longest
groupByDay = varaible.groupby('time_of_day')['duration_minutes'].mean()
print_line(groupByDay)
