
@author: charlotte
"""

import csv

class Baby:
    year=0
    name=''
    present=0
    sex=''
babies=[]
with open("baby-names.csv") as file:#read file and put col in category
    rows = csv.reader(file)
    next(rows)
    for row in rows:
        c = Baby()
        c.year = int(row[0])
        c.name = row[1]
        c.percent = float(row[2])
        c.sex = row[3]
        babies.append(c)    
        
print('step 1: Most Peak Given Name')
print("============================")

maxpercent=max(babies,key=lambda x:x.percent)
print('Name '+maxpercent.name+' was given to '+str(maxpercent.percent*100)+'% of babies in '+str(maxpercent.year))

print('')
print('step 2: Recommendation Name')
print("================================")

sexput = input('Gender (girl/boy):')
styput = input('Style (modern/classic/none):')
if styput == 'modern':
       modern = list(filter(lambda x:x.year >= 1990 and x.sex == sexput,babies))
       max1 = max(modern,key=lambda x:x.percent)#fint the max in the same sex and year.
       print('We suggest the name '+max1.name)
elif styput == 'classic':
       classic = list(filter(lambda x:x.year < 1990 and x.sex == sexput ,babies))
       max2 = max(classic,key=lambda x:x.percent)
       print('We suggest the name '+max2.name)
elif styput == 'none':
       none = list(filter(lambda x:x.sex == sexput,babies))
       max3 = max(none,key=lambda x:x.percent)
       print('We suggest the name '+max3.name)
print('\n')        

print('step 3: Popularity Graph')
print("========================")
nameput1 = input('Name:')
sexput1 = input('Gender (girl/boy):')
filtered=list(filter(lambda x:x.name == nameput1 and x.sex == sexput1, babies))#filter all the same sex and sex name category
x = list(map(lambda x:x.year,filtered))
y = list(map(lambda x:x.percent,filtered))
import matplotlib.pyplot as plt
plt.xticks = ([1880,1900,1920,1940,1960,1980,2000,2010])
plt.yticks = ([0.00,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09])
plt.plot(x,y)


























