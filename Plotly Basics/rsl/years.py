import plotly.graph_objects as go
import pandas as pd
import textwrap

df = pd.read_csv('../../data/years.csv')

# x = [16, 13, 11, 6, 5]
# y = ['Comprehension', 'Engagement', 'Usability', 'Information', 'Memorability']

data = [go.Bar(
    x=df['Year'].dropna(axis=0, how='any'),
    y=df['Cantidad'].dropna(axis=0, how='any'),
    orientation='v',
    # customdata=df['Subcriterios'].apply(lambda t: "<br>".join(textwrap.wrap(t, width=15))),
    # hovertemplate='<b>Subcriteria:</b><br><br>%{customdata}<extra></extra>',
    text=df['Cantidad'],
    textfont=dict(
        color='white',
        size=22,
    ),
    marker=dict(
        color='#2ABBC1',
        line=dict(
            color='#2ABBC1',
            width=5

        )
    ),
    hoverlabel=dict(
        namelength=-1,
        bgcolor='white',
        bordercolor='black',
        font=dict(
            color='black',
            size=18
        )

    ),
)]

layout = go.Layout(font=dict(
    size=18,
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
# fig.show()
fig.write_image("../../data/fig0.png", width=5.9*300, height=2.75*300, scale=1.05)