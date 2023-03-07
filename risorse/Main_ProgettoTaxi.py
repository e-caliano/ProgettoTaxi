from input import richiesta_utente
from elaborazione import merge_and_filter
from elaborazione import durata
from elaborazione import merge_and_filter_per_tutti_i_quartieri
from elaborazione import min_max_durata
from post_elaborazione import export_to_csv
from post_elaborazione import export_min_max_durata_to_csv
from plot import plot_durata_massima_per_quartiere


df_list, quartieri_list = richiesta_utente()
merged_list = merge_and_filter(df_list, quartieri_list)
x=durata(merged_list)
merged_list2 = merge_and_filter_per_tutti_i_quartieri(df_list)
y = durata(merged_list2)
z,t = min_max_durata(y)
export_to_csv(x, 'Durate_per_quartiere_cercato_ufficiale')
export_min_max_durata_to_csv(z,t,'Durate_minima_e_massima')
plot_durata_massima_per_quartiere(y, 'Istogramma')