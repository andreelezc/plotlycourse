import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Read dataframe
df = pd.read_csv('../data/mpg.csv')

# List of columns available to select and plot
features = df.columns

# Create Dash app
app = dash.Dash()

# Create app layout
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='x-axis',
            options=[{'label': i, 'value': i} for i in features],
            value='displacement'
        )
    ],
        style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='y-axis',
            options=[{'label': i, 'value': i} for i in features],
            value='acceleration'
        )
    ],
        style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(
        id='features-graphic'
    )],
    style={'padding': 10})


@app.callback(Output(component_id='feature-graphic', component_property='figure'),
              [Input(component_id='x-axis', component_property='value'),
               Input(component_id='y-axis', component_property='value')])
def update_graph(xaxis_name, yaxis_name):
    # Create figure
    trace = go.Scatter(
        x=df[xaxis_name],
        y=df[yaxis_name],
        text=df['name'],
        mode='markers',
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5, 'color': 'white'}
        })

    layout = go.Layout(
        title='Multiple Inputs',
        xaxis={'title': xaxis_name},
        yaxis={'title': yaxis_name},
        hovermode='closest'
    )

    return {'data': [trace], 'layout': layout}


if __name__ == '__main__':
    app.run_server()
