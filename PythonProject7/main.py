# This is a sample Python script.
from ftplib import print_line

import pandas as pd
import numpy as np
import seaborn as sns

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings


DataFrame = pd.read_csv('team17_callcenter.csv')
#finding out the resolution rate by call type
resolved = DataFrame.groupby('call_type')['resolved'].value_counts(normalize=True)
print_line(resolved)


#Finding the which time of day is the longest
groupByDay = DataFrame.groupby('time_of_day')['duration_minutes'].mean()
print_line(groupByDay)

#finding the percentage of resolved high priority calls
highPriority = DataFrame.groupby('priority')['resolved'].value_counts(normalize=True)*100
print_line(highPriority)

#Looking at how agent work load varies by time of day


#Spotting any missing values in our dataFrame:
isNull = DataFrame.isnull().sum()
print_line(isNull)
#Getting the percentages of the null variables
isNull = DataFrame.isnull().mean()*100
print_line(isNull)


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