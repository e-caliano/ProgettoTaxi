import pandas as pd
import os
import matplotlib.pyplot as plt

def export_to_csv(merged_list, filename):
    """
    :param merged_list: lista di dataframes
    :param filename: stringa
    """
    # Concatena tutti i DataFrame nella lista in uno unico
    merged_df = pd.concat(merged_list, axis=0, ignore_index=True)
    # Ordina il DataFrame in ordine decrescente di durata
    merged_df.sort_values(by='durata', ascending=False, inplace=True)
    # Scrive il file CSV nella cartella output
    merged_df.to_csv("output/" + filename + '.csv', index=False)
    print(f"I dati sono stati esportati nel file {filename}.csv")

def export_min_max_durata_to_csv(min_durata, max_durata,filename):
    """
    :param min_durata: dataframe
    :param max_durata: dataframe
    :param filename: stringa
    """
    # Concatena i DataFrame di min_durata e max_durata in uno unico
    df = pd.concat([min_durata, max_durata], axis=0, ignore_index=True)
    # Scrive il file CSV nella cartella output
    df.to_csv("output/" + filename + '.csv', index=False)
    print(f"I dati sono stati esportati nel file {filename}.csv")

