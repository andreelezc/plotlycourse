#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc


# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv('../data/OldFaithful.csv')

# Create plotly figure
trace = go.Scatter(x=df['X'],
                   y=df['Y'],
                   mode='markers')

layout = go.Layout(title='Scatter Plot',
                   xaxis={'title': 'Duration'},
                   yaxis={'title': 'Interval'})

# Create a Dash layout that contains a Graph component:
app.layout = html.Div(children=[
    html.H1('Simple Dashboard Excercise'),
    dcc.Graph(id='sp', figure={'data': [trace],
                               'layout': layout})
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()