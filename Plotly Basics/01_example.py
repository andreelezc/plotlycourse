import pandas as pd
import textwrap

df_nodes = pd.read_csv('../data/nodos.csv')
df_links = pd.read_csv('../data/links.csv')

df_nodes['Info'] =(df_nodes['Info'].apply(textwrap.wrap, width=30))

print(df_nodes['Info'])