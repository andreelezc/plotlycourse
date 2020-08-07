#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['mpg'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/200))]

# create a layout with a title and axis labels
layout = go.Layout(title='Bubble Chart Exercise',
                   xaxis=dict(title='Miles per Galon'),
                   yaxis=dict(title='Acceleration'),
                   hovermode='closest')


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)