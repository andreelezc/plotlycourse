import plotly.graph_objects as go
import pandas as pd
import textwrap

df = pd.read_csv('../../data/criterios-subcriterios.csv')

# x = [16, 13, 11, 6, 5]
# y = ['Comprehension', 'Engagement', 'Usability', 'Information', 'Memorability']

data = [go.Bar(
    y=df['Criterio'].dropna(axis=0, how='any'),
    x=df['Cantidad'].dropna(axis=0, how='any'),
    orientation='h',
    customdata=df['Subcriterios'].apply(lambda t: "<br>".join(textwrap.wrap(t, width=15))),
    hovertemplate='<b>Subcriteria:</b><br><br>%{customdata}<extra></extra>',
    text=df['Cantidad'],
    textfont=dict(
        color='white',
        size=25,
    ),
    marker=dict(
        color='rgba(237, 118, 109, 1)',
        line=dict(
            color='rgba(237, 118, 109, 1)',
            width=5

        )
    ),
    hoverlabel=dict(
        namelength=10,
        bgcolor='white',
        bordercolor='black',
        font=dict(
            color='black',
            size=16
        )

    ),
)]

layout = go.Layout(font=dict(
    size=25,
    color='black'
),
    xaxis=dict(
        visible=False,
    ),
    yaxis=dict(
        # ticks='outside',
        # tickcolor='white',
        # ticklen=10
        # autorange='reversed'
        categoryorder='total ascending'
    ),
    margin_pad=20,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    clickmode='event+select'

)

fig = go.Figure(data=data, layout=layout)
fig.show()
fig.write_image("../../data/fig3.png", width=4*300, height=2*300, scale=1)