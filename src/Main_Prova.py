from input_prova import *
from post_elaborazione_prova import *
from plot_prova import plot_durata_massima_per_quartiere

lista_df1, lista_df2, durata_minima, durata_massima = richiesta_utente()
export_to_csv(lista_df1,'Dataframe_durate')
export_min_max_durata_to_csv(durata_minima, durata_massima, 'Dataframe_minimi_e_massimi')
plot_durata_massima_per_quartiere(lista_df2, 'Plot')