import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='text-input',
              placeholder='Type something...',
              value='',
              style={'fontSize': 24}),
    html.Button(id='submit-button',
                n_clicks=0,
                children='Submit',
                style={'fontSize': 24}),
    html.Div(id='text-output',
             style={'padding': 10, 'fontSize': 24})
])


@app.callback(Output('text-output', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('text-input', 'value')])
def update_output(n_clicks, text):
    return "You've entered {}. The button has been clicked {} times.".format(text, n_clicks)


if __name__ == '__main__':
    app.run_server()
