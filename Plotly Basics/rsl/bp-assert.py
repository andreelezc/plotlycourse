import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../../data/bp-assert.csv')


data = [go.Bar(
    x=df['ID'].dropna(axis=0, how='any'),
    y=df['Cantidad'].dropna(axis=0, how='any'),
    orientation='v',
    text=df['Cantidad'],
    textfont=dict(
        color='black',
        size=18,
    ),
    textposition='outside',
    textangle=0,
    marker=dict(
        color='#2ABBC1',
        line=dict(
            color='#2ABBC1',
            width=2

        )
    ),
    hoverlabel=dict(
        namelength=-1,
        bgcolor='white',
        bordercolor='black',
        font=dict(
            color='black',
            size=16
        )

    ),
)]

layout = go.Layout(font=dict(
    size=14,
    color='black'
),
    yaxis=dict(
        visible=False,
    ),
    xaxis=dict(
        type='category'
    ),

    margin_pad=5,

    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',

    clickmode='event+select'

)

fig = go.Figure(data=data, layout=layout)
fig.show()

# fig.write_image("../../data/fig2.png", width=6.5*300, height=2.5*300, scale=1)  # 15x5 cm at 300dpi