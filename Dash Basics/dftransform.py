import pandas as pd

casos = pd.read_csv(r'C:\Users\Andre\JupyterNotebook\datasets\reportes.csv')

casos['fecha'] = pd.to_datetime(casos['fecha'], format='%Y/%m/%d')
casos['fecha'] = casos['fecha'].dt.date

mapping_dict = {'fecha': 'Fecha', 'positivos': 'Positivos', 'positivos_acumulado': 'Positivos Acumulados'}
casos = casos.rename(mapping_dict, axis=1)

casos = casos[['Fecha', 'Positivos', 'Positivos Acumulados']]
casos.to_csv('casos.csv', index=False)