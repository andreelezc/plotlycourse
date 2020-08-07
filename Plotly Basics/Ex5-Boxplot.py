#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:

import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go


# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')
print(df)

# take two random samples of different sizes:
s1 = np.random.choice(df['rings'], 10, replace=False)
s2 = np.random.choice(df['rings'], 10, replace=False)


# create a data variable with two Box plots:
trace1 = go.Box(y=s1, name='Sample 1')
trace2 = go.Box(y=s2, name='Sample 2')

data = [trace1, trace2]

# add a layout
layout = go.Layout(title='Boxplot Exercise')


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)