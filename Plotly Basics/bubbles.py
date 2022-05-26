import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go


df = pd.read_csv('../data/mpg.csv')

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight'] / 100,
                               color=df['cylinders'],
                               showscale=True))]

layout = go.Layout(title='Bubble Chart',
                   xaxis={'title': 'Horsepower'},
                   yaxis=dict(title='Miles per Galon'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
fig.update_layout(template='ggplot2')
pyo.plot(fig)
