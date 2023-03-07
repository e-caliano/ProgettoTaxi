import pandas as pd
import os



def carica_informazioni(anno, mese, path):
    """
    :param anno: stringa
    :param mese: stringa
    :param path: stringa
    :return: dataframe
    """
    #funzione per leggere il file .parquet in base all'anno e mese specificati
    nome_file = f'yellow_tripdata_{anno}-{mese}.parquet'
    file_path = f'{path}/{nome_file}'
    return pd.read_parquet(file_path)


def richiesta_utente():
    """
    :return: lista di dataframe, lista di stringhe
    """
    #Chiedo all'utente di inserire anno, mese e path assoluto della repository Data
    anno = input('inserisci anno: ')
    mese = input('inserisci mese: ')
    path = input('inserisci path assoluto: ')
    quartieri = input('Inserisci i quartieri della quale vuoi conoscere le durate: ' )
    #creo una lista di quartieri
    quartieri_list = []
    #visualizzo le la stringa non è vuota
    if quartieri.strip():
        #Se la condizione dell' if è vera divido i quartieri con una virgola creando una lista
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




