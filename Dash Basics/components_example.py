import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt


app = dash.Dash()
app.layout = html.Div(children=[
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'California', 'value': 'CA'},
        ],
        value='NYC'),

    html.Label('Slider'),
    dcc.Slider(min=-10,
               max=10,
               step=0.5,
               value=0,
               marks={i: i for i in range(-10, 10)}),

    html.Label('Radio items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'California', 'value': 'CA'},
        ],
        value='NYC'),

    html.Label('Date picker'),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt(1997, 2, 8)
    )
])

if __name__ == '__main__':
    app.run_server()
