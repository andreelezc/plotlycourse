import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

# Read in the dataframe
df = pd.read_csv('../data/gapminderDataFiveYear.csv')

# Create Dash app
app = dash.Dash()

# List of years for the dropdown
year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

# Create app layout
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',
                 options=year_options,
                 value=df['year'].min()
                 )
])


# Connect selected year from dropdown to figure
@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='year-picker', component_property='value')])
def update_figure(selected_year):
    # filter df to select only data from selected year
    filtered_df = df[df['year'] == selected_year]

    # create traces for every continent
    traces = []

    for cont in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == cont]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=cont
        ))

    layout = go.Layout(title='My Plot',
                       xaxis={'title': 'GDP Per Capita',
                              'type': 'log'},
                       yaxis={'title': 'Life Expectancy'})

    return {'data': traces, 'layout': layout}


# Run app
if __name__ == '__main__':
    app.run_server()
