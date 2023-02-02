
import pandas as pd
import matplotlib.pyplot as plt 

# sort data 
poki = pd.read_csv('pokemon_data.csv', index_col='#')
poki.rename(columns = {'Type 1' : 'Type_1', 'Type 2' : 'Type_2', 'Sp. Atk' : 'SP_Atk', 'Sp. Def' : 'SP_Def'}, inplace=True)
poki.drop('Generation', 1, inplace=True)

def legendary_among_best_defenders() -> None:

    '''percentage of legendary poekmons among best defenders'''

    defense = poki.sort_values(['Defense'], ascending=[0]).head(50)
    legos = defense.loc[defense['Legendary'] == True].count()[-1]
    non_legos = 50 - legos

    fig = plt.subplots()
    plt.title(
              'Percentage of legendary Pokemons among 50 best defenders', 
              fontsize=18, 
              fontweight='bold'
             )

    labels = ['Legendary', 'Non-legendary']
    colors = ['#FB9300', '#30E3DF']

    plt.pie(
            [legos, non_legos], 
            labels=labels, 
            colors=colors, 
            autopct='%.2f %%'
           )

    plt.legend()
    plt.show()
    
legendary_among_best_defenders()