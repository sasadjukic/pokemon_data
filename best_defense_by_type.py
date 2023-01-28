
import pandas as pd
import matplotlib.pyplot as plt 
from collections import Counter

# sort data 
poki = pd.read_csv('pokemon_data.csv', index_col='#')
poki.rename(columns = {'Type 1' : 'Type_1', 'Type 2' : 'Type_2', 'Sp. Atk' : 'SP_Atk', 'Sp. Def' : 'SP_Def'}, inplace=True)
poki.drop('Generation', 1, inplace=True)

def highest_defense():

    ''' returns class 'collections.Counter' '''

    tops = poki.sort_values(['Defense'], ascending=[0]).head(50)
    top_data = tops['Type_1'].tolist()
    data = Counter(top_data)

    return data

def best_defense_bar_chart(counter) -> None:

    '''
        shows how many times a certain type occurs among 50 best defenders
        condition: must be in top 50 minimum 2 times
    '''

    labels = [k for k, v in counter.items() if v >= 2]
    values = [v for v in counter.values() if v >= 2]
    colors = [
              '#FF6D28', '#65647C', '#D0B8A8', 
              '#0D4C92', '#473C33', '#645CBB', 
              '#EAE0DA', '#B6E388'
             ]

    fig = plt.subplots()
    plt.bar(labels, values, color=colors)
    plt.yticks([x for x in range(0, 14)])
    plt.xticks(rotation='vertical')
    plt.ylabel(
               'Top 50 placements', 
               fontsize=12, 
               fontweight='bold'
              )

    plt.suptitle(
                 'Pokemon Best Defenders by Type 1', 
                 fontsize=16, 
                 fontweight='bold'
                )

    plt.title(
              '*must appear in top 50 defending stat at least twice', 
              fontsize=8
             )

    plt.show()

defense = highest_defense()
best_defense_bar_chart(defense)