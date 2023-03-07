import pandas as pd
import os
import matplotlib.pyplot as plt

def export_to_csv(merged_list, filename):
    # Concatena tutti i DataFrame nella lista in uno unico
    merged_df = pd.concat(merged_list, axis=0, ignore_index=True)
    # Ordina il DataFrame in ordine decrescente di durata
    merged_df.sort_values(by='durata', ascending=False, inplace=True)
    # Scrive il file CSV
    merged_df.to_csv("output/" + filename + '.csv', index=False)
    print(f"I dati sono stati esportati nel file {filename}.csv")

def export_min_max_durata_to_csv(min_durata, max_durata,filename):
    # Concatena i DataFrame di min_durata e max_durata in uno unico
    df = pd.concat([min_durata, max_durata], axis=0, ignore_index=True)
    # Scrive il file CSV
    df.to_csv("output/" + filename + '.csv', index=False)
    print(f"I dati sono stati esportati nel file {filename}.csv")


import matplotlib.pyplot as plt


def plot_durata_massima_per_quartiere(merged_list, filename):
    # Calcolo la durata massima per ogni quartiere
    durate_massime = []
    quartieri = []
    for df in merged_list:
        quartiere_durata_massima = df.groupby(['borough'])['durata'].max()
        quartieri.extend(quartiere_durata_massima.index.tolist())
        durate_massime.extend(quartiere_durata_massima.tolist())

    # Creo il DataFrame con i dati da plottare
    data_to_plot = pd.DataFrame({'quartiere': quartieri, 'durata_massima': durate_massime})
    # Plottaggio dell'istogramma. Do una dimensione scelta
    plt.figure(figsize=(12,6))
    plt.bar(data_to_plot['quartiere'], data_to_plot['durata_massima'])
    #ruoto l'etichetta dell'asse x di 90 gradi
    plt.xticks(rotation=90)
    plt.title('DURATE MASSIME DEI QUARTIERI DI NEW YORK')
    plt.xlabel('Quartiere')
    plt.ylabel('Durata massima (s)')
    # Salvo l'istogramma come file png
    plt.savefig("output/" + filename + '.png')
    print(f"L'istogramma è stato salvato nel file {filename}.png")
