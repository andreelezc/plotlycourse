import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='my-input-comp',
        placeholder='Enter something',
        type='text',
        value=''
    ),

    html.Div(id='my-div')
])


@app.callback(Output(component_id='my-div', component_property='children'),  # the property you want to affect
              [Input(component_id='my-input-comp', component_property='value')])  # the property you'll take as input
def update_output_div(input_value):
    return "You entered: {}".format(input_value)


if __name__ == '__main__':
    app.run_server()
