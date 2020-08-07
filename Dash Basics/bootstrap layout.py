# # App Layout
# app.layout = dbc.Container(fluid=True, children=[
#     ## Top
#     html.H1(config.name, id="nav-pills"),
#     navbar,
#     html.Br(),html.Br(),html.Br(),
#     ## Body
#     dbc.Row([
#         ### input + panel
#         dbc.Col(md=3, children=[
#             inputs,
#             html.Br(),html.Br(),html.Br(),
#             html.Div(id="output-panel")
#         ]),
#         ### plots
#         dbc.Col(md=9, children=[
#             dbc.Col(html.H4("Forecast 30 days from today"), width={"size":6,"offset":3}),
#             dbc.Tabs(className="nav nav-pills", children=[
#                 dbc.Tab(dcc.Graph(id="plot-total"), label="Total cases"),
#                 dbc.Tab(dcc.Graph(id="plot-active"), label="Active cases")
#             ])
#         ])
#     ])
# ])