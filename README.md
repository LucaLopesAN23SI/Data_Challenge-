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

    Duration      Resolved %
         1         72.131148
         2         68.253968
         3         76.136364
         4         70.512821
         5         77.108434
         6         77.142857
         7         70.000000
         8         75.757576
         9         77.049180
        10         82.258065
        11         71.428571
        12         73.584906
        13         70.270270
        14         73.333333
        15         71.052632
        16         73.529412
        17         77.272727
        18         85.714286
        19         77.777778
        20         80.952381
        21         70.588235
        22         66.666667
        23         63.636364
        24         90.000000
        25         71.428571
        26         75.000000
        27         83.333333
        28         50.000000
        29         50.000000
        30         50.000000
        32        100.000000
        33        100.000000
        35        100.000000
        37        100.000000
        45        100.000000
        48        100.000000

Results: No. There does not seem to be a correlation between the call duration and customer satisfaction, as shown in both rows 20 and 28. 
Row 20 contains a significantly higher customer satisfaction score then rows 21,21,23.
Rows 28, 29 and 30 all have mixed reviews with the success having the same chance of a coin flip. 
Rows 32 and above dont show an accurate representation since there are no, idk.....