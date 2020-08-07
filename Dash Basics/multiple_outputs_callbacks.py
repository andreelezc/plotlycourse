import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import base64

# Read in dataframe
df = pd.read_csv('../data/wheels.csv')


# Encode images
def encode_image(image_file):
    encoded = base64.b64decode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


# Create Dash app
app = dash.Dash()

# Create app layout
app.layout = html.Div([
    dcc.RadioItems(
        id='wheels',
        options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
        value=2
    ),
    html.Div(
        id='wheels-output'
    ),
    html.Hr(),
    dcc.RadioItems(
        id='colors',
        options=[{'label': i, 'value': i} for i in df['color'].unique()],
        value='red'
    ),
    html.Div(
        id='colors-output'
    ),
    html.Img(
        id='display-image',
        src='children',
        height=300
    )],
    style={'fontFamily': 'helvetica', 'fontSize': 18})


@app.callback(
    Output(component_id='wheels-output', component_property='children'),
    [Input(component_id='wheels', component_property='value')]
)
def callback_wheels(wheels_choice):
    return "You've selected {}".format(wheels_choice)


@app.callback(
    Output(component_id='colors-output', component_property='children'),
    [Input(component_id='colors', component_property='value')]
)
def callback_colors(colors_choice):
    return "You've selected: {}".format(colors_choice)


@app.callback(
    Output(component_id='display-img', component_property='src'),
    [Input(component_id='wheels', component_property='value'),
     Input(component_id='colors', component_property='value')]
)
def callback_img(wheels_choice, colors_choice):
    path = '../data/Images'
    mask = (df['wheels'] == wheels_choice) & (df['color'] == colors_choice)
    return encode_image(path+df[mask]['image'].values[0])


if __name__ == '__main__':
    app.run_server()
