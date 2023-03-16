#!/usr/bin/env python
# coding: utf-8

# In[0]:


import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd


# In[1]:


# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache') 


# In[2]:


year, grand_prix, session = 2023, 'Bahrain', 'R'

race = ff1.get_session(year, grand_prix, session)
race.load() # This is new with Fastf1 v.2.2

# This is how it used to be:
# race = race.load_laps(with_telemetry=True)


# In[3]:


driver_1, driver_2, driver_3, driver_4 = 'VER', 'ALO', 'SAI', 'HAM'


# In[4]:


# Convert laptimes to seconds
race.laps['LapTimeSeconds'] = race.laps['LapTime'].dt.total_seconds()

# Laps can now be accessed through the .laps object coming from the session
laps_driver_1 = race.laps.pick_driver(driver_1)
laps_driver_2 = race.laps.pick_driver(driver_2)
laps_driver_3 = race.laps.pick_driver(driver_3)
laps_driver_4 = race.laps.pick_driver(driver_4)

# Select the fastest lap
fastest_driver_1 = laps_driver_1.pick_fastest()
fastest_driver_2 = laps_driver_2.pick_fastest()
fastest_driver_3 = laps_driver_3.pick_fastest()
fastest_driver_4 = laps_driver_4.pick_fastest()

# Retrieve the telemetry and add the distance column
telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()
telemetry_driver_3 = fastest_driver_3.get_telemetry().add_distance()
telemetry_driver_4 = fastest_driver_4.get_telemetry().add_distance()


# In[5]:


# Make sure whe know the team name for coloring
team_driver_1 = fastest_driver_1['Team']
team_driver_2 = fastest_driver_2['Team']
team_driver_3 = fastest_driver_3['Team']
team_driver_4 = fastest_driver_4['Team']


# In[6]:


plot_size = [15, 15]
plot_title = f"{race.event.year} {race.event.EventName} - {race.name} - Lap times comparison and fastest lap telemetry"
plot_ratios = [7, 3, 2, 1, 1, 2, 1]
plot_filename = plot_title.replace(" ", "") + ".png"


# In[7]:


# Make plot a bit bigger
plt.rcParams['figure.figsize'] = plot_size

# Create subplots with different sizes
fig, ax = plt.subplots(7, gridspec_kw={'height_ratios': plot_ratios})

# Set the plot title
ax[0].title.set_text(plot_title)


# Lap time chart
ax[0].plot(laps_driver_1['LapNumber'], laps_driver_1['LapTimeSeconds'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[0].plot(laps_driver_2['LapNumber'], laps_driver_2['LapTimeSeconds'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[0].plot(laps_driver_3['LapNumber'], laps_driver_3['LapTimeSeconds'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[0].plot(laps_driver_4['LapNumber'], laps_driver_4['LapTimeSeconds'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[0].set(ylabel='Laptime (s)')
ax[0].set(xlabel='Lap')
ax[0].legend(loc="upper right")
ax[0].grid()

# Speed trace
ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[1].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Speed'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[1].plot(telemetry_driver_4['Distance'], telemetry_driver_4['Speed'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[1].set(ylabel='Speed')
ax[1].legend(loc="lower right")

# Throttle trace
ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[2].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Throttle'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[2].plot(telemetry_driver_4['Distance'], telemetry_driver_4['Throttle'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[2].set(ylabel='Throttle')

# Brake trace
ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[3].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Brake'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[3].plot(telemetry_driver_4['Distance'], telemetry_driver_4['Brake'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[3].set(ylabel='Brake')

# Gear trace
ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[4].plot(telemetry_driver_3['Distance'], telemetry_driver_3['nGear'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[4].plot(telemetry_driver_4['Distance'], telemetry_driver_4['nGear'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[4].set(ylabel='Gear')

# RPM trace
ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[5].plot(telemetry_driver_3['Distance'], telemetry_driver_3['RPM'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[5].plot(telemetry_driver_4['Distance'], telemetry_driver_4['RPM'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[5].set(ylabel='RPM')

# DRS trace
ax[6].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[6].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[6].plot(telemetry_driver_3['Distance'], telemetry_driver_3['DRS'], label=driver_3, color=ff1.plotting.team_color(team_driver_3))
ax[6].plot(telemetry_driver_4['Distance'], telemetry_driver_4['DRS'], label=driver_4, color=ff1.plotting.team_color(team_driver_4))
ax[6].set(ylabel='DRS')
ax[6].set(xlabel='Lap distance (meters)')

plt.savefig(plot_filename, dpi=300)
plt.show()


# In[8]:


# Print lap times
print("Lap times for Max Verstappen")
print(laps_driver_1.LapTime)
print()
print("Lap times for Fernando Alonso")
print(laps_driver_2.LapTime)
print()
print("Lap times for Carlos Sainz")
print(laps_driver_3.LapTime)
print()
print("Lap times for Lewis Hamilton")
print(laps_driver_4.LapTime)


# In[ ]:




