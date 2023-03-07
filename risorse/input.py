import pandas as pd
import os
from elaborazione import merge_and_filter
from elaborazione import durata
from elaborazione import merge_and_filter_per_tutti_i_quartieri
from post_elaborazione import min_max_durata


def carica_informazioni(anno, mese, path):
    nome_file = f'yellow_tripdata_{anno}-{mese}.parquet'
    file_path = f'{path}/{nome_file}'
    return pd.read_parquet(file_path)


def richiesta_utente():
    #Chiedo all'utente di inserire anno, mese e path assoluto della repository Data
    anno = input('inserisci anno: ')
    mese = input('inserisci mese: ')
    path = input('inserisci path assoluto: ')
    quartieri = input('Inserisci i quartieri della quale vuoi conoscere le durate: ' )
    #creo una lista di quartieri
    quartieri_list = []
    if quartieri.strip():
        #do la possibilità di non inserire niente per vedere ogni quartiere
        quartieri_list = quartieri.split(',')
        # rimuovo gli spazi iniziali e finali dai nomi dei quartieri
        quartieri_list = [quartiere.strip() for quartiere in quartieri_list]
    #creo lista vuota per i dataframe
    df_list = []
    # Itera attraverso i mesi richiesti e carica i dati corrispondenti in un dataframe
    for mesi in mese.split(','):
        df = carica_informazioni(anno, mesi, path)
        df_list.append(df)
    return df_list, quartieri_list



df_list,quartieri_list = richiesta_utente()
lookup_df = pd.read_csv(r'C:\Users\gaeta\OneDrive\Documenti\ProgettoTaxi\ProgettoTaxi\Data\taxi+_zone_lookup.csv')
merged_list = merge_and_filter(df_list, lookup_df, quartieri_list)
x=durata(merged_list)
print(x)
merged_list2 = merge_and_filter_per_tutti_i_quartieri(df_list, lookup_df)
#applico la durata alla lista con tutti i quartieri
y = durata(merged_list2)
#applico la funzione di ricerca di minimo e massimo
z = min_max_durata(y)
print(z)