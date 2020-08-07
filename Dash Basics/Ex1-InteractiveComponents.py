#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-10,
        max=10,
        step=0.5,
        value=[-3, 3],
        marks={i: str(i) for i in range(-10, 11)}
    ),
    html.H1(id='range-output')
])


@app.callback(
    Output('range-output', 'children'),
    [Input('range-slider', 'value')]
)
def update_output(value_list):
    return value_list[0] * value_list[1]


if __name__ == '__main__':
    app.run_server()








# Create a Dash callback:






# Add the server clause:
