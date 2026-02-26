# Data_Challenge-

## Overview 
    Hello. This is the documentation of our findings in this data analysis challenge
    
The purpose of this repository is to analyze the data of the call center for the issues or future improvements in customer support 

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

    