
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# sort data 
poki = pd.read_csv('pokemon_data.csv', index_col='#')
poki.rename(columns = {'Type 1' : 'Type_1', 'Type 2' : 'Type_2', 'Sp. Atk' : 'SP_Atk', 'Sp. Def' : 'SP_Def'}, inplace=True)
poki.drop('Generation', 1, inplace=True)

def legendaries():

    '''
        finds legendary / non-legendaries stats
        returns pandas dataframe
    '''

    legendary = poki.groupby(['Legendary']).mean().round(2)
    return legendary

def compare_stats_bar_chart(stats) -> None:

    '''compares stats between legendary and non-legendary Pokemon'''

    legendaries = stats.iloc[1].tolist()
    non_legendaries = stats.iloc[0].tolist()
    labels = ['HP', 'Attack', 'Defense', 'SP_Atk', 'SP_Def', 'Speed']

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    non_legos = ax.bar(
                        x - width/2, 
                        non_legendaries, 
                        width, 
                        label='Non-Legendary', 
                        color='#FBC252'
                      )
    legos = ax.bar(
                    x + width/2, 
                    legendaries, 
                    width, 
                    label='Legendary', 
                    color='#58287F'
                   )

    ax.set_ylabel('Values', fontsize=20)
    ax.set_title(
                 'Pokemon Legendary vs. Non-Legendary Skill Averages', 
                 fontsize=20, 
                 fontweight='bold', 
                 fontname='Tahoma'
                 )

    ax.set_xticks(x, labels, fontsize=10)
    ax.legend()

    ax.bar_label(non_legos, padding=3)
    ax.bar_label(legos, padding=3)

    fig.tight_layout()
    plt.show()

legos = legendaries()
compare_stats_bar_chart(legos)