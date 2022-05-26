import pandas as pd
import textwrap
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.io as pio

pio.kaleido.scope.mathjax = None

df_nodes = pd.read_csv('../../data/nodos.csv')
df_links = pd.read_csv('../../data/links.csv')

data = [go.Sankey(
    valueformat='.0f',
    orientation='h',

    # NODES
    node=dict(
        label=df_nodes['Label'].dropna(axis=0, how='any'),
        color=df_nodes['Color'],
        customdata=df_nodes["Info"].apply(lambda t: "<br>".join(textwrap.wrap(t, width=40))),
        hovertemplate='%{customdata}<extra></extra>',
        hoverlabel=dict(
            namelength=-1,
            bgcolor='white',
            bordercolor='black',
            font=dict(
                color='black',
                size=16
            )
        ),
        pad=15,
        thickness=25,
        line=dict(
            color='black',
            width=0,
        ),
    ),

    # LINKS
    link=dict(
        source=df_links['Source'].dropna(axis=0, how='any'),
        target=df_links['Target'].dropna(axis=0, how='any'),
        value=df_links['Value'].dropna(axis=0, how='any'),
        color=df_links['Link Color'].dropna(axis=0, how='any'),
        hoverlabel=dict(
            font=dict(
                color='black',
                size=14
            ),
        )
    )
)]

layout = go.Layout(
                   # title='<b>Best Practices Categorization</b><br>Subtitle',
                   font=dict(
                       size=25,
                   ),
                   paper_bgcolor='rgba(0,0,0,0)',
                   plot_bgcolor='rgba(0,0,0,0)',
                   )

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
# fig.write_image("../../data/fig1.png", width=3.14*300, height=5.11*300, scale=1)  # 13x8 cm at 300dpi
