import matplotlib.pyplot as plt
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

#group by location
covid_2 = covid.groupby(['location'])['total_cases', 'new_cases', 'total_deaths', 'new_deaths'].sum()
covid_2['case_fatality_rate'] = covid_2['total_deaths'] / covid_2['total_cases']

#%matplotlib inline

#draw scatter-a
plt.scatter(covid_2.iloc[:,[1]],covid_2.iloc[:,[4]],color='green')

plt.xlim(0,25000000)
plt.ylim(0,0.3)
plt.ylabel("facility rate")
plt.xlabel("new cases")
plt.grid(True)

plt.savefig("scatter-a.png")

#log new_cases
import math
log_new_cases = []
for i in covid_2['new_cases']:
    if i == 0.0:
        log_new_cases.append(0)
    else:
        log_new_cases.append(math.log(i,10))
        
#draw scatter-b
plt.scatter(log_new_cases,covid_2.iloc[:,[4]],color='green')

plt.xlim(0,10)
plt.ylim(0,0.3)
plt.ylabel("facility rate")
plt.xlabel("ln(new cases)")
plt.grid(True)

plt.savefig("scatter-b.png")