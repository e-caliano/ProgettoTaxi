import pandas as pd
import os

def min_max_durata(merged_list):
    # Lista per le durate minime e massime
    durata_minima = []
    durata_massima = []

    for df in merged_list:
        durata_minima.append(df.loc[df['durata'].idxmin()])
        durata_massima.append(df.loc[df['durata'].idxmax()])

    # Trova la maggiore tra le durate massime e la minore tra le durate minime
    durata_minima = pd.DataFrame(durata_minima)
    durata_massima = pd.DataFrame(durata_massima)
    min_durata = durata_minima.loc[durata_minima['durata'].idxmin()]
    max_durata = durata_massima.loc[durata_massima['durata'].idxmax()]

    return min_durata, max_durata
