import pandas as pd



def merge_and_filter(df, lista_quartieri):
    """
    :param df: dataframe
    :param lista_quartieri:lista
    :return: merged_df : dataframe
    """
    #leggo il file csv
    lookup_df = pd.read_csv('../Data/taxi+_zone_lookup.csv')

    #Cambio il nome delle colonne del file parquet
    df.rename(columns={"PULocationID": "id"}, inplace=True)

    # rinomina le colonne nel dataframe di lookup
    lookup_df.rename(columns={"LocationID": "id", "Borough": "borough"}, inplace=True)

    #Faccio merge sulle colonne
    merged_df = pd.merge(df, lookup_df, on= 'id')

    #seleziono solo le colonne richieste
    merged_df = merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]]

    #filtro per i quartieri di interesse
    merged_df = merged_df[merged_df['borough'].isin(lista_quartieri)]

    #elimino duplicati e valori Nan nelle series più importanti e lascio solo le series principali ai nostri calcoli
    merged_df.drop_duplicates(inplace=True)
    merged_df = merged_df.dropna(subset=['id', 'borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    # Lascio solo le series senza righe con 'NaN'
    merged_df = merged_df.loc[merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]].notna().all(axis=1)]

    # Il dataframe non deve contenere il borough 'Unknown'
    merged_df = merged_df[merged_df['borough'] != 'Unknown']

    #restituisco la lista dei dataframe mergeati
    return merged_df


def merge_and_filter_per_tutti_i_quartieri(df):
    """
    :param df : dataframe
    :return merged_df : dataframe
    """
    #sto studiando il caso in cui voglio tutti i quartieri
    lookup_df = pd.read_csv('../Data/taxi+_zone_lookup.csv')
    merged_list = []
    df.rename(columns={"PULocationID": "id"}, inplace=True)

    lookup_df.rename(columns={"LocationID": "id", "Borough": "borough"}, inplace=True)
    #svolgo le stesse attività del merge_and_filter, ma con la differenza che voglio utilizzare tutti i quartieri, non solo quelli scelti
    merged_df = pd.merge(df, lookup_df, on='id')
    merged_df = merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]]
    merged_df.drop_duplicates(inplace=True)
    merged_df = merged_df.dropna(subset=['id', 'borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    merged_df = merged_df.loc[merged_df[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]].notna().all(axis=1)]
    merged_df = merged_df[merged_df['borough'] != 'Unknown']
    merged_list.append(merged_df)

    return merged_df


def durata(merged_df):
    """
    :param merged_df: dataframe
    :return: merged_df : dataframe
    """

    # Converto le date in formato datetime
    merged_df['tpep_pickup_datetime'] = pd.to_datetime(merged_df['tpep_pickup_datetime'])
    merged_df['tpep_dropoff_datetime'] = pd.to_datetime(merged_df['tpep_dropoff_datetime'])
    # Calcolo la durata in secondi come differenza tra le due date
    merged_df['durata'] = (merged_df['tpep_dropoff_datetime'] - merged_df['tpep_pickup_datetime']).dt.total_seconds()
    # Elimina le righe in cui la durata è uguale a 0 o minore di 0
    merged_df.drop(merged_df[merged_df['durata'] <= 0].index, inplace=True)
    #ordino la lista per durata crescente
    merged_df.sort_values(by=['durata'], inplace=True)

    return merged_df


def min_max_durata(merged_df):
    """
    :param merged_df: dataframe
    :return: durata_minima : dataframe
            durata_massima : dataframe
    """
    # durata minima e massima
    durata_minima = merged_df.loc[merged_df['durata'].idxmin()]
    durata_massima = merged_df.loc[merged_df['durata'].idxmax()]

    return durata_minima, durata_massima

