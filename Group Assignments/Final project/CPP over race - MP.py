#!/usr/bin/env python
# coding: utf-8

# In[1]:


# usual suspects
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import contextily as ctx
import plotly.express as px

# new for data viz
import seaborn as sns

# to explore point patterns
from pointpats import centrography
from matplotlib.patches import Ellipse
import numpy as np


# # California Power Plant (CPP) Map

# In[2]:


# load cpp data
cpp = gpd.read_file('California_Power_Plants_MP Cleaned 3.1.21.csv')


# ## CPP data exploration and cleaning

# In[3]:


type(cpp)


# In[4]:


cpp.shape


# In[5]:


cpp.head(10)


# In[6]:


cpp.info


# In[7]:


cpp.columns = ['Plant_ID',
 'Name',
 'MW',
 'Gross_MWh',
 'Net_MWh',
 'Fuel_Type',
 'Status',
 'Online_Year',
 'REAT_ID',
 'County',
 'State',
 'Renewable_Energy',
 'Jobs',
 'Senate_District',
 'Assembly_District',
 'Congressional_District',
 'CES30_PercentileRange',
 'CES30_Percentile',
 'Lon',
 'Lat',
 'Operation_Job',
 'Capacity_Factor',
 'Income_Percent',
 'Project_Location',
 'geometry']


# In[8]:


# define variable with desired columns 
desired_columns = [
 'Name',
 'MW',
 'Fuel_Type',
 'Status',
 'County',
 'State',
 'Renewable_Energy',
 'Jobs',
 'CES30_PercentileRange',
 'CES30_Percentile',
 'Lon',
 'Lat',
 'Income_Percent',
 'Project_Location',
 'geometry']

# redefine dataframe with just desired columns.
cpp_trim = cpp[desired_columns].copy()

# check out the new dataframe! 
cpp_trim


# In[9]:


# convert coordinates  and jobs to floats. 
cpp_trim.Lon = cpp_trim.Lon.astype('float')
cpp_trim.Lat = cpp_trim.Lat.astype('float')
cpp_trim.Jobs = cpp_trim.Jobs.astype('float')


# In[10]:


# convert cpp data to geodataframe
cpp_trim = gpd.GeoDataFrame(cpp_trim, 
                         crs='EPSG:4326',
                         geometry=gpd.points_from_xy(cpp_trim.Lon, cpp_trim.Lat))

cpp_trim.head(5)


# In[11]:


# check crs type
cpp_trim.crs


# In[12]:


# create dataframe for fossil fuel energy
cpp_trim_ff = cpp_trim[cpp_trim.Renewable_Energy != '1']


# In[13]:


# create dataframe for renewable energy
cpp_trim_ce = cpp_trim[cpp_trim.Renewable_Energy == '1']


# # CalEnviroScore Demographics (CES)

# In[14]:


# load CES data
gdf_ces = gpd.read_file('CES3June2018Update.shp')


# ## CES data exploration and cleaning

# In[15]:


type(gdf_ces)


# In[16]:


gdf_ces.crs


# In[17]:


#define variable with desired columns 
columns_to_keep = ['tract', 'pop2010', 'California', 'ZIP', 'City', 'Longitude', 'Latitude', 'CIscore', 'CIscoreP', 'edu', 'eduP', 'pov', 'povP', 'unemp', 'unempP', 'Pop_11_64_', 'Elderly_ov', 'Hispanic_p', 'White_pct', 'African_Am', 'Native_Ame', 'Asian_Amer', 'Other_pct', 'geometry']

#redfine dataframe with desired columns 
gdf_ces = gdf_ces[columns_to_keep]

# rename some columns
gdf_ces.columns = ['tract', 'pop2010', 'California', 'ZIP', 'City', 'Longitude', 'Latitude', 'CIscore', 'CIscoreP', 'edu', 'eduP', 'pov', 'povP', 'unemp', 'unempP', 'Pop_11_64_', 'Elderly_ov', 'Percent_Hispanic', 'Percent_White', 'Percent_Black', 'Percent_Native_American', 'Percent_AAPI', 'Other_pct', 'geometry']

# check to make sure 
gdf_ces.head()


# In[18]:


# check work
gdf_ces.dtypes


# ## Tracts by race

# In[ ]:


gdf_ces.plot(figsize=(12,10),
             column='Percent_Hispanic',
             legend=True,
             cmap='Blues',
             scheme='NaturalBreaks')


# In[ ]:


gdf_ces.plot(figsize=(12,10),
             column='Percent_White',
             legend=True,
             cmap='Blues',
             scheme='NaturalBreaks')


# In[ ]:


gdf_ces.plot(figsize=(12,10),
             column='Percent_Black',
             legend=True,
             cmap='Blues',
             scheme='NaturalBreaks')


# In[ ]:


gdf_ces.plot(figsize=(12,10),
             column='Percent_Native_American',
             legend=True,
             cmap='Blues',
             scheme='NaturalBreaks')


# In[ ]:


gdf_ces.plot(figsize=(12,10),
             column='Percent_AAPI',
             legend=True,
             cmap='Blues',
             scheme='NaturalBreaks')


# In[19]:


# create list of races
ces_races = ['Percent_Hispanic', 'Percent_White', 'Percent_Black','Percent_Native_American','Percent_AAPI']


# In[20]:


gdf_ces.plot(figsize=(12,10),
             column='Percent_AAPI',
             legend=True,
             cmap='Blues',
             scheme='NaturalBreaks')


# In[22]:


# convert both to web mercator
gdf_ces = gdf_ces.to_crs(epsg=3857)

cpp_trim = cpp_trim.to_crs(epsg=3857)


# In[23]:


# convert column to integer
cpp_trim['CES30_Percentile'] = pd.to_numeric(cpp_trim['CES30_Percentile'])


# In[24]:


cpp_trim.dtypes


# In[25]:


# convert column to integer
cpp_trim['MW'] = pd.to_numeric(cpp_trim['MW'])


# In[27]:


# make race subplots
f, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 15))
# Make the axes accessible with single indexing
axs = axs.flatten()
# Start a loop over all the variables of interest
for i, col in enumerate(ces_races):
    # select the axis where the map will go
    ax = axs[i]
    # Plot the map
    gdf_ces.plot(column=col, ax=ax, scheme='Quantiles', 
            linewidth=0, cmap='Greens')
    # Powerplant map
    cpp_trim.plot(ax=ax, # this also puts it in the same ax plot
            color='red',
            markersize=3,
            alpha=0.2)
    # Remove axes
    ax.set_axis_off()
    # Set the axis title to the name of variable being plotted
    ax.set_title(col)
# Display the figure
plt.show()


# In[28]:


# for loop to plot powerplants across races
for i, col in enumerate(ces_races):
    fig, ax = plt.subplots(figsize=(5,5))
    
    gdf_ces.plot(ax=ax,
                 column=col,
                 scheme='Quantiles', 
                 linewidth=0,
                 legend=True,
                 cmap='YlGn')

    cpp_trim.plot(ax=ax,
            color='red',
            markersize=3,
            alpha=0.5)
    
    ax.set_axis_off()
    
    ax.set_title(col)
    
plt.show()


# In[29]:


# for loop to plot fossil fuel plants across races
for i, col in enumerate(ces_races):
    fig, ax = plt.subplots(figsize=(10,10))
    
    gdf_ces.plot(ax=ax,
                 column=col,
                 scheme='naturalbreaks', 
                 linewidth=0.1,
                 edgecolor="#04253a",
                 legend=True,
                 cmap='Blues')

    cpp_trim_ff.plot(ax=ax,
            color='red',
            markersize=7,
            alpha=0.5)
    
    ax.set_axis_off()
    
    ax.set_title(str(col) + ' Fossil Fuel Plants')
    
plt.show()


# In[30]:


# for loop to plot clean energy plants across races
for i, col in enumerate(ces_races):
    fig, ax = plt.subplots(figsize=(10,10))
    
    gdf_ces.plot(ax=ax,
                 column=col,
                 scheme='naturalbreaks', 
                 linewidth=0.1,
                 edgecolor="#04253a",
                 legend=True,
                 cmap='Blues')

    cpp_trim_ce.plot(ax=ax,
            color='red',
            markersize=5,
            alpha=0.5)
    
    ax.set_axis_off()
    
    ax.set_title(str(col) + ' Clean Energy Plants')
    
plt.show()


# In[31]:


# scatterplot of power plants by CES
fig = px.scatter(cpp_trim,
                 x = 'CES30_Percentile',
                 y = 'MW',
                 color = 'CES30_Percentile',
                 hover_name = 'County',
                 size = 'MW')

fig.show()


# In[ ]:


# write to html for storymap display
fig.write_html("MWbyCES.html")


# In[ ]:




