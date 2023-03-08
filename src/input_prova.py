import pandas as pd
import os
from elaborazione_prova import merge_and_filter
from elaborazione_prova import durata
from elaborazione_prova import min_max_durata
from elaborazione_prova import merge_and_filter_per_tutti_i_quartieri


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


def inserisci_dati():
    """
    :return: anno: stringa
            lista_mesi = lista di stringhe
            lista_quartieri = lista di stringhe
            path = stringa
    """
    anno = input("Inserisci l'anno: ")
    mese = input('inserisci mese: ')
    quartieri = input('Inserisci i quartieri della quale vuoi conoscere le durate: ')
    path = input('inserisci path assoluto: ')

    #separo i mesi dalla virgola
    lista_mesi = mese.split(',')
    lista_mesi = [mes.strip() for mes in lista_mesi]

    # creo una lista di quartieri
    lista_quartieri = []

    # visualizzo se la stringa quartieri non è vuota
    if quartieri.strip():
        # Se la condizione dell' if è vera divido i quartieri con una virgola creando una lista
        lista_quartieri = quartieri.split(',')
        # rimuovo gli spazi iniziali e finali dai nomi dei quartieri
        lista_quartieri = [quartiere.strip() for quartiere in lista_quartieri]

    return anno, lista_mesi, lista_quartieri, path


def richiesta_utente():
    """
    :return: lista_df1 : lista di dataframe
            lista_df2 : lista di dataframe
            durata_minima : dataframe
            durata_massima : dataframe
    """
    #creo una lista vuota per il dataframe da riempire con i quartieri scelti ed una lista per tutti i quartieri
    lista_df1 = []
    lista_df2 = []
    #chiamo la funzione inserisci_dati
    anno, lista_mesi, lista_quartieri, path = inserisci_dati()
    #per ogni mese inserito svolgo tutte le operazioni ed infine appendo tutto nella lista
    for i in lista_mesi:
        #prima il dataframe con i quartieri scelti
        df1 = carica_informazioni(anno, i, path)
        merged_df1 = merge_and_filter(df1, lista_quartieri)
        merged_df1 = durata(merged_df1)

        #dataframe con tutti i quartieri
        df2 = carica_informazioni(anno, i, path)
        merged_df2 = merge_and_filter_per_tutti_i_quartieri(df2)
        merged_df2 = durata(merged_df2)
        durata_minima, durata_massima = min_max_durata(merged_df2)

        lista_df1.append(merged_df1)
        lista_df2.append(merged_df2)


    return lista_df1, lista_df2, durata_minima, durata_massima




