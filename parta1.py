import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

import pandas as pd
import argparse
from datetime import datetime
covid = pd.read_csv('data/owid-covid-data.csv',encoding = 'ISO-8859-1')

#filter dataset
covid['bool'] = covid['date'].str.contains('2020')

c = 0
for i in covid['bool']:
    if i == False:
        covid = covid.drop([c])
    c += 1

#extract month information
month = []
for i in covid['date']:
    month.append(i[5:7])

covid['month'] = month

#calculate sum
covid_1 = covid.groupby(['location','month'])['total_cases', 'new_cases', 'total_deaths', 'new_deaths'].sum()

#calculate fatality rate
covid_1['case_fatality_rate'] = covid_1['total_deaths'] / covid_1['total_cases']

#save as .csv file
covid_1.to_csv("owid-covid-data-2020-monthly.csv")