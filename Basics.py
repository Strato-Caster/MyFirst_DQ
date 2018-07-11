
# coding: utf-8

# In[3]:


import csv
f=open("guns.csv")
g=csv.reader(f)
data=list(g)
print(data[0:5])


# In[4]:


headers=data[0]
data=data[1:]
print(data[0:5])


# In[5]:


years=[row[1] for row in data]
year_counts={}
for row in years:
    if row in year_counts:
        year_counts[row]=year_counts[row]+1
    else:
        year_counts[row]=1
print(year_counts)


# In[6]:


import datetime
dates=[datetime.datetime(year=int(row[1]),month=int(row[2]),day=1) for row in data]


# In[7]:


print(dates[:5])


# In[8]:


date_counts={}
for row in dates:
    if row in date_counts:
        date_counts[row]=date_counts[row]+1
    else:
        date_counts[row]=1
print(date_counts)


# In[9]:


sexes = [row[5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex] += 1

print(sex_counts)


# In[10]:



races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
print(race_counts)


# In[11]:


import csv
f=open("census.csv")
g=csv.reader(f)
census=list(g)
print(census)


# In[12]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[ ]:


intents=[row[3] for row in data]
races=[row[7] for row in data]
homicide_race_counts={}
for i,race in enumerate(races):
    if intents[i]=="Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] +=1
        else:
            homicide_race_counts[race]=1
race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk
    
    

