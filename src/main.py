import pandas as pd
from datetime import datetime
import os
import pathlib
import datetime
import time
import platform
df_lookup = pd.read_csv('/Users/edoardocaliano/Desktop/PrgettoTaxi/Data/taxi+_zone_lookup.csv')


def load_file(path):
    """
    Funzione per la lettura dei file .parquet o .csv e creazione del dataframe
    :param path: str
    :return: dataframe
    """
    # estrazione dell'estensione del file
    extension = path.split(".")[-1]

    if extension == "csv":
        # se l'estensione è csv, carichiamo il DataFrame dal file CSV
        df = pd.read_csv(path)
    elif extension == "parquet":
        # se l'estensione è parquet, carichiamo il DataFrame dal file PARQUET
        df = pd.read_parquet(path, engine='pyarrow')
    else:
        # se l'estensione non è supportata, solleviamo un'eccezione
        raise ValueError("Estensione del file non supportata. Sono supportati solo i file CSV e PARQUET.")

    return df


def merge(df):
    """
    Funzione per unire il dataframe yellow_tripdata con il dataframe lookup
    :param df: dataframe
    :return: dataframe
    """


    # rinominazione delle series id di entrambi i dataframe
    df.rename(columns={
        "VendorID": "id"
    }, inplace=True)
    df_lookup.rename(columns={
        "LocationID": "id",
        "Borough": "borough"
    }, inplace=True)

    # facciamo un merge dei due dataframe collegandoli grazie ai rispettivi id in comune
    df_total = pd.merge(left=df, right=df_lookup, on="id")
    # creazione del dataframe di interesse per i calcoli sui tragitti
    df = df_total[["id", "borough", "tpep_pickup_datetime", "tpep_dropoff_datetime"]]

    return df


def filter(df):
    """
    Funzione per il filtraggio del dataframe totale: eliminazione dei valori duplicati e delle righe con valori nulli
    :param df: dataframe
    :return: dataframe
    """
    df = df.drop_duplicates()
    df = df.dropna(subset=['id', 'borough', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])

    return df


def durata(df):
    """
    Funzione per trovare la durata di ogni corsa
    :param df: dataframe
    :return: dataframe
    """
    # convertiamo le colonne delle date in oggetti datetime
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # calcoliamo la durata di ogni corsa in secondi
    df['durata_corsa'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()

    df = df[df['durata_corsa'] > 0]
    return df


def viaggio_più_breve(df):
    """
    :param df: dataframe
    :return: riga del dataframe
    """

    # troviamo l'indice della riga che contiene il valore minimo della serie
    indice_riga_minimo = df["durata_corsa"].idxmin()

    # selezioniamo la riga del dataframe che contiene il valore minimo
    riga_minimo = df.loc[indice_riga_minimo]

    return riga_minimo


def viaggio_più_lungo(df):
    """
    :param df: dataframe
    :return: riga del dataframe
    """

    # troviamo l'indice della riga che contiene il valore massimo della serie
    indice_riga_massimo = df["durata_corsa"].idxmax()

    # selezioniamo la riga del dataframe che contiene il valore massimo
    riga_massimo = df.loc[indice_riga_massimo]

    return riga_massimo



