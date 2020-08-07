import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# Create dash app
app = dash.Dash()

# Read in a dataframe
df = pd.read_csv('../data/2018WinterOlympics.csv')

# Create traces
trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold',
                marker={'color': '#FFD700'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker={'color': '#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker={'color': '#CD7F32'})

# Define a figure layout
layout = go.Layout(title='Bar Plot')

# Colors dictionary for styling
colors = {'text': '#171717',
          'background': '#FFFFFF'}

# Define dash layout
app.layout = html.Div(children=[
    html.H1('Plotly Dashboard with Python', style={'textAlign': 'center',
                                                   'background': colors['background']}),
    dcc.Graph(id='barplot',
              figure={
                  'data':[trace1, trace2, trace3],
                  'layout':[layout]
              })

])

if __name__ == '__main__':
    app.run_server()
