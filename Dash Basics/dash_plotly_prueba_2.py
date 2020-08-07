import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

# Create dash app
app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash()

# Read in a dataframe
df = pd.read_csv('../data/casos.csv')

# Create traces
trace1 = go.Scatter(x=df['Fecha'],
                    y=df['Positivos Acumulados'],
                    mode='lines+markers',
                    name='Positivos Acumulados',
                    hoverinfo='x+y',
                    marker={'size': 8},
                    line={'color': '#d92d1a',
                          'width': 3}
                    )

trace2 = go.Scatter(x=df['Fecha'],
                    y=df['Positivos'],
                    mode='lines+markers',
                    name='Positivos Diarios',
                    hoverinfo='x+y',
                    marker={'size': 8},
                    line={'color': '#10397a',
                          'width': 3}
                    )

# Define a figure layout
layout = go.Layout(title={'text': '<b>Gráficos de líneas con Dash</b>',
                          'font': {'family': 'Arial',
                                   'size': 24,
                                   'color': '#171717'},
                          'xanchor': 'auto',
                          },
                   xaxis={'title': 'Fecha'},
                   yaxis={'title': 'Número de casos'})

# Colors dictionary for styling
colors = {'text': '#171717',
          'background': '#FFFFFF'}

# Define dash layout
app.layout = html.Div(children=[
    html.H1('Dashboard con Plotly en Python', style={'textAlign': 'center',
                                                     'background': colors['background']}),
    dcc.Graph(id='lineplot',
              figure={
                  'data': [trace1, trace2],
                  'layout': layout
              })

])

if __name__ == '__main__':
    app.run_server()
