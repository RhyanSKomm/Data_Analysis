import pandas as pd

df = pd.read_csv('data.csv')

alunos_por_cidade = df['cidade'].value_counts()

media_por_cidade = df.groupby('cidade')['nota'].mean()

