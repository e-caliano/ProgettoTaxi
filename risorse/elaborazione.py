import pandas as pd
import os


def merge_and_filter(df_list, quartieri_list):
    """
    :param df_list: lista
    :param quartieri_list:lista
    :return: lista di dataframes
    """
    #leggo il file csv
    lookup_df = pd.read_csv('../Data/taxi+_zone_lookup.csv')

    #creo una lista vuota così posso tenere tutti i file singolarmente mergiati
    merged_list =[]
    #Cambio il nome delle colonne dei file parquet
    for i in df_list:
        i.rename(columns={"PULocationID": "id"}, inplace=True)

    # rinomina le colonne nel dataframe di lookup
    lookup_df.rename(columns={"LocationID": "id", "Borough": "borough"}, inplace=True)


    for i in df_list:
        #Faccio merge sulle colonne
        merged_df = pd.merge(i, lookup_df, on= 'id')

        #seleziono solo le colonne richieste
        merged_df = merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]]

        #filtro per i quartieri di interesse
        merged_df = merged_df[merged_df['borough'].isin(quartieri_list)]

        #elimino duplicati e valori Nan nelle series più importanti e lascio solo le series principali ai nostri calcoli
        merged_df.drop_duplicates(inplace=True)
        merged_df = merged_df.dropna(subset=['id', 'borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
        # Lascio solo le series senza righe con 'NaN'
        merged_df = merged_df.loc[merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]].notna().all(axis=1)]

        # Il dataframe non deve contenere il borough 'Unknown'
        merged_df = merged_df[merged_df['borough'] != 'Unknown']

        #aggiungo i dataframes mergeati
        merged_list.append(merged_df)


    #restituisco la lista dei dataframe mergeati
    return merged_list


def merge_and_filter_per_tutti_i_quartieri(df_list):
    """
    :param df_list: lista di dataframes
    :return: lista di dataframes
    """
    #sto studiando il caso in cui voglio tutti i quartieri
    lookup_df = pd.read_csv('../Data/taxi+_zone_lookup.csv')
    merged_list = []
    for i in df_list:
        i.rename(columns={"PULocationID": "id"}, inplace=True)

    lookup_df.rename(columns={"LocationID": "id", "Borough": "borough"}, inplace=True)
    #svolgo le stesse attività del merge_and_filter, ma con la differenza che voglio utilizzare tutti i quartieri, non solo quelli scelti
    for i in df_list:
        merged_df = pd.merge(i, lookup_df, on='id')
        merged_df = merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]]
        merged_df.drop_duplicates(inplace=True)
        merged_df = merged_df.dropna(subset=['id', 'borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
        merged_df = merged_df.loc[merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]].notna().all(axis=1)]
        merged_df = merged_df[merged_df['borough'] != 'Unknown']
        merged_list.append(merged_df)

    return merged_list


def durata(merged_list):
    """
    :param merged_list: lista di dataframes
    :return: lista di dataframes
    """
    for df in merged_list:
        # Converto le date in formato datetime
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        # Calcolo la durata in secondi come differenza tra le due date
        df['durata'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()
        # Elimina le righe in cui la durata è uguale a 0
        df.drop(df[df['durata'] <= 0].index, inplace=True)
        #ordino la lista per durata crescente
        df.sort_values(by=['durata'], inplace=True)

    return merged_list


def min_max_durata(merged_list):
    """
    :param merged_list: lista di dataframes
    :return: due dataframes
    """
    # Lista per le durate minime e massime
    durata_minima = []
    durata_massima = []

    for df in merged_list:
        #cerco, per ogni dataframe, la lista con valore minimo e massimo
        durata_minima.append(df.loc[df['durata'].idxmin()])
        durata_massima.append(df.loc[df['durata'].idxmax()])

    #Trasformo le liste con le durate in dataframe
    # Trova la maggiore tra le durate massime e la minore tra le durate minime
    durata_minima = pd.DataFrame(durata_minima)
    durata_massima = pd.DataFrame(durata_massima)
    min_durata = durata_minima.loc[durata_minima['durata'].idxmin()]
    max_durata = durata_massima.loc[durata_massima['durata'].idxmax()]

    return min_durata, max_durata
