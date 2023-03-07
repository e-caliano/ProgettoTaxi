import pandas as pd
import os
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
    plt.savefig(filename + '.png')
    print(f"L'istogramma è stato salvato nel file {filename}.png")
