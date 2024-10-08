import pandas as pd
from functions.create_dataframe import create_dataframe_example

# load example table 
df = create_dataframe_example(seed = 83)

# filter by columns 
df [['Nome', 'Turno']]
df[['Turno', 'Nome']].head(n = 6)
df[['Turno', 'Nome']].tail()

# filter by filter 
df['Nota_1_Prova']
df[['Nota_1_Prova']]

df[
    (df['Nota_1_Prova'] > 80) & 
    (df ["Turno"] == "Noite")
   
   ] 

df.query("Nota_1_Prova > 80 and Turno == 'Noite'")

# Combine rows and columns 
df \
    .query("Nota_1_Prova > 80 and Turno == 'Noite'") \
    [['Nome']] 

# aggregate     
df \
    .groupby('Turno') \
    .agg(
        Nota_1_media = ('Nota_1_Prova', 'mean'),
        Nota_2_media = ('Nota_2_Prova', 'mean')
    ) \
    .reset_index()
    

# change or create columns 
df \
    .groupby('Turno') \
    .agg(
        Nota_1_media = ('Nota_1_Prova', 'mean'),
        Nota_2_media = ('Nota_2_Prova', 'mean')
    ) \
    .reset_index() \
    .assign(
        Nota_1_media = lambda x: round(x['Nota_1_media'], 2),
        Nota_2_media = lambda x: round(x['Nota_1_media'], 2),
        Nota_media_soma = lambda x: x ['Nota_1_media'] + x['Nota_2_media']   
    )

