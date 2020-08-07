import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51, 204, 153)',
                       symbol='circle',
                       line={'width': 2}
                   ))]

layout = go.Layout(title='First Plot',
                   xaxis={'title': 'X AXIS'},
                   yaxis=dict(title='Y AXIS'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')

