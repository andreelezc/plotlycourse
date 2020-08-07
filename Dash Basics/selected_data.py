import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

# Read dataframe
df = pd.read_csv('../data/wheels.csv')

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='scatter',
            figure={
                'data': [
                    go.Scatter(
                        x=df['color'],
                        y=df['wheels'],
                        dy=1,
                        mode='markers',
                        marker={
                            'size': 12,
                            'color': 'rgb(51,204,153)',
                            'line': {'width': 2}
                        }
                    )
                ],
                'layout': go.Layout(
                    title='Wheels & Colors Scatterplot',
                    xaxis={'title': 'Color'},
                    yaxis={'title': '# of Wheels', 'nticks': 3},
                    hovermode='closest'
                )
            }
        )], style={'width': '30%', 'float': 'left'}),

    html.Div([
        html.Pre(id='selected-data', style={'paddingTop': 35})
    ], style={'width': '30%'})
])


@app.callback(
    Output('selected-data', 'children'),
    [Input('scatter', 'selectedData')])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)


if __name__ == '__main__':
    app.run_server()
