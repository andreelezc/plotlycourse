import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])

df = pd.read_csv('../data/mpg.csv')

app.layout = dbc.Container(fluid=True, children=[
    # Top
    html.H1('Updating Graph on Interactions', style={'textAlign': 'center', 'margin-top': 20}),

    # Body
    dbc.Row([
        dbc.Col(md=6, children=[
            dcc.Graph(id='scatter-graph',
                      figure={'data': [go.Scatter(x=df['model_year'],
                                                  y=df['mpg'],
                                                  mode='markers',
                                                  text=df['name'],
                                                  hoverinfo='text')],
                              'layout': go.Layout(
                                  title={'text': 'MPG Dataset',
                                         'x': 0.5,
                                         'y': 0.9,
                                         'xanchor': 'center',
                                         'yanchor': 'top'},

                                  xaxis={'title': 'model year'},
                                  yaxis={'title': 'miles per gallon'},
                                  hovermode='closest'
                              )})
        ]),
        dbc.Col(md=4, children=[
            dcc.Graph(id='line-graph',
                      figure={'data': [go.Scatter(x=[0, 1],
                                                  y=[0, 1],
                                                  mode='lines',
                                                  line={'width': 5})],
                              'layout': go.Layout(title='acceleration',
                                                  xaxis={'visible': False},
                                                  yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]},
                                                  margin={'l': 0},
                                                  height=300
                                                  )
                              })
        ]),
        dbc.Col(md=2, children=[
            dcc.Markdown(id='stats-output')
        ])
    ])

])


@app.callback(
    Output('line-graph', 'figure'),
    [Input('scatter-graph', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    fig = {
        'data': [go.Scatter(
            x=[0, 1],
            y=[0, 60 / df.iloc[v_index]['acceleration']],
            mode='lines',
            line={'width': 2 * df.iloc[v_index]['cylinders']}
        )],
        'layout': go.Layout(
            title=df.iloc[v_index]['name'],
            xaxis={'visible': False},
            yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]},
            margin={'l': 0},
            height=300
        )
    }
    return fig


@app.callback(
    Output('stats-output', 'children'),
    [Input('scatter-graph', 'hoverData')])
def stats_callback(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
            {} cylinders
            {}cc displacement
            0 to 60mph in {} seconds
            """.format(df.iloc[v_index]['cylinders'],
                       df.iloc[v_index]['displacement'],
                       df.iloc[v_index]['acceleration'])
    return stats


if __name__ == '__main__':
    app.run_server()
