#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd


# In[2]:


# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache') 


# In[3]:


year, grand_prix, session = 2023, 'Australia', 'R'

race = ff1.get_session(year, grand_prix, session)
race.load() # This is new with Fastf1 v.2.2

# This is how it used to be:
# race = race.load_laps(with_telemetry=True)


# In[4]:


driver_1, driver_2, driver_3 = 'VER', 'HAM', 'ALO'


# In[36]:


# Convert laptimes to seconds
race.laps['LapTimeSeconds'] = race.laps['LapTime'].dt.total_seconds()

# To get accurate laps only, we exclude in- and outlaps and safety car laps
laps = race.laps.loc[(race.laps['IsAccurate'] == True) & (race.laps['LapNumber'] != 10)]

# Laps can now be accessed through the .laps object coming from the session
laps_driver_1 = laps.pick_driver(driver_1)
laps_driver_2 = laps.pick_driver(driver_2)
laps_driver_3 = laps.pick_driver(driver_3)


# In[37]:


# Make sure whe know the team name for coloring
team_driver_1 = laps_driver_1['Team']
team_driver_2 = laps_driver_2['Team']
team_driver_3 = laps_driver_3['Team']


# In[38]:


plot_size = [15, 15]
plot_title = f"{race.event.year} {race.event.EventName} - {race.name} - Lap times comparison"
plot_filename = plot_title.replace(" ", "") + ".png"


# In[52]:


# Make plot a bit bigger
plt.rcParams['figure.figsize'] = plot_size

# Set the plot title
plt.title(plot_title)

# Lap time chart
plt.plot(laps_driver_1['LapNumber'], laps_driver_1['LapTimeSeconds'], label=driver_1, color='blue')
plt.plot(laps_driver_2['LapNumber'], laps_driver_2['LapTimeSeconds'], label=driver_2, color='cyan')
plt.plot(laps_driver_3['LapNumber'], laps_driver_3['LapTimeSeconds'], label=driver_3, color='green')
plt.ylabel('Laptime (s)')
plt.xlabel('Lap')
plt.legend(loc="upper right")
plt.grid()
plt.savefig(plot_filename, dpi=300)
plt.show()


# In[79]:


# Print lap times
print("List of lap times. In/Out laps and safety car laps are omitted.")
print()
print("Max Verstappen")
print(laps_driver_1[['LapTime', 'LapNumber']])
print()
print("Lewis Hamilton")
print(laps_driver_2[['LapTime', 'LapNumber']])
print()
print("Fernando Alonso")
print(laps_driver_3[['LapTime', 'LapNumber']])


# In[ ]:




