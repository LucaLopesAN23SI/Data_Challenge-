# Video
https://drive.google.com/file/d/1hmfan-eteGmjJHCOUJsKxs8hqeAlcYRh/view?usp=drive_link

# Data Challenge

## Overview 
    Hello. This is the documentation of our findings in this data analysis challenge
    
The purpose of this repository is to analyze the data of the call center for the issues or future improvements in customer support 

For more information, please look at the notebook provided in this repository, it contains more accurate values, graphs and code used using pandas for our solutions

## Data Notebook
The notebook contains all of the information regarding graphs, explaining the duration of time per agent in the call center, customer satisfaction and which of the periods of time receive the most amount of calls.
## Missing Values Analysis:
Upon initial exploration we identified a couple of missing values in these 2 columns:

    Wait Time Minutes: 45 : 4.09%
    Customer Satisfaction: 54 : 4.91%

## Other findings 
We found flat lines in our "duration per minutes" graph which represent how many customers have hung up before support could get a hold. 
We believe this data is also important as it tells us that they need to improve their customer retention training.
### Cleaning:
We deleted the rows with the null values since both wait time mins and customer satisfaction both have a null representation of less than 5%.
This is because when the ammount of inconsistencies are less than 5%, this wouldnt affect the data if it were to be deleted.
The modified data is also included in the repo.
## Analysis:
### Resolution rate by call type
The resolution rate per type goes as followed:

    Call Type     Resolution Rate 
    Complaint          77.50%
    Inquiry            74.73%
    Sales              75.78%
    Support            71.78%

The call center seems to have a successfully high amount of successfully resolved complaints
### Customer Satisfaction 
Here lies the chart of customer satisfaction compared with their wait time (per minutes):

    Customer            Wait Time
    Satisfaction         Period 
     1.0/5.0              2.38m    
     2.0/5.0              2.68m
     3.0/5.0              2.96m
     4.0/5.0              2.57m
     5.0/5.0              2.55m
The data shows that wait time peaks at the 3 stars.
This means that wait time is not a factor thataffects customer satisfaction.
### Longest Average Call Duration
Percentages of high priority calls:

    Time of Day         Average
    Afternoon            9.25%
    Evening              9.01
    Morning             10.28

From that we find out that mornings have the longest call duration, being 10 minutes ad 28 seconds on average.

### Average Agent Workload Per Time of Day
Here is a look at the average agent workload per time of day:

    Time of       Average Agent
      Day             Calls
    Afternoon         12.10
    Evening           6.26
    Morning           9.85

Even though the morning has the longest average call duration, the afternoon period is has the highest agent workload average with each agent receiving an average of 12.10 calls every afternoon.

### Is there a correlation between Call Duration and Resolution ?
Rates of successful calls vs their Duration:

    Resolved     Duration
      False        9.44m
      True         9.60m

Rates of resolved call per minute of  waiting

    Duration  Resolution Rate  Call Count
        1        72.131148          61
        2        68.253968          63
        3        76.136364          88
        4        70.512821          78
        5        77.108434          83
        6        77.142857          70
        7        70.000000          70
        8        75.757576          66
        9        77.049180          61
        10        82.258065         62
        11        71.428571         42
        12        73.584906         53
        13        70.270270         37
        14        73.333333         30
        15        71.052632         38
        16        73.529412         34
        17        77.272727         22
        18        85.714286         21
        19        77.777778          8
        20        80.952381         21
        21        70.588235         17
        22        66.666667          6
        23        63.636364         11
        24        90.000000         10
        25        71.428571          7
        26        75.000000          8
        27        83.333333          6
        28        50.000000          2
        29        50.000000          2
        30        50.000000          4
        32       100.00000           2
        33       100.000000          1
        35       100.000000          1
        37       100.000000          1
        38         0.000000          1
        40         0.000000          1
        45       100.000000          1
        48       100.000000          1

        Correlation: 0.010085
        P-values: 0.738279
Results: With the p-value is greater than 0.05, we fail to resject the null hypothesis
This indicates that an extremely weak and insignificant relationship betwee the call duration and the resolution
Also, the average duration of the resolved calls(9.60 min) differes from unresolved calls (9.44) by only 16 seocnds, which means there was no meaningful difference.
Call duration doesn't appear to be a a relible way to predict the success of the calls
