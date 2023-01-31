
import pandas as pd
import matplotlib.pyplot as plt 

# sort data 
poki = pd.read_csv('pokemon_data.csv', index_col='#')
poki.rename(columns = {'Type 1' : 'Type_1', 'Type 2' : 'Type_2', 'Sp. Atk' : 'SP_Atk', 'Sp. Def' : 'SP_Def'}, inplace=True)
poki.drop('Generation', 1, inplace=True)

def double_type_share_of_best_defense() -> None:

    '''percentage of poekmons with two types(Type 1 and Type 2) among best defenders'''

    defense = poki.sort_values(['Defense'], ascending=[0]).head(50)
    both_types = len(defense['Type_2'].dropna().tolist())
    single_type = 50 - both_types

    fig = plt.subplots()
    plt.title(
              'Percentage of dual type Pokemons among 50 best Defenders', 
              fontsize=18, 
              fontweight='bold'
             )

    labels = ['Dual Types', 'Single Type']
    colors = ['#FB9300', '#674188']

    plt.pie(
            [both_types, single_type], 
            labels=labels, 
            colors=colors, 
            autopct='%.2f %%'
           )

    plt.legend(loc='upper left')
    plt.show()

double_type_share_of_best_defense()