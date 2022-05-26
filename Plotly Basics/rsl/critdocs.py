import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('../../data/critdocs.csv', na_filter=False)
df.rename(columns={df.columns[0]: " "}, inplace=True)

data = [go.Table(
    header=dict(
        values=list(df.columns),
        align='left',
        fill_color='#F4F4F4',
        font=dict(
            size=10
        )
    ),
    cells=dict(
        values=df.transpose().values.tolist(),
        fill_color=['#F4F4F4', 'white'],
        line=dict(
            color=['white', '#F4F4F4']
        ),
        font=dict(size=10)
    ),
)]

layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
fig.show()
