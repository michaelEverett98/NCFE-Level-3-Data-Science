# ==================================================
#               Unit 2 - part 2 assessment
# ==================================================

# ==================================================
# Task 1: Download two datasets. Describe where they were sourced from, what they contain, and why they can be joined together.
# ==================================================

# The datasets were sourced from Kaggle, an open dataset platform, and contain two different tables of data pertaining to Pokemon. One of them contains all of the available Pokemon species in the mainline games, with information such as name, typing, abilities, and battle stats. The other contains the moves available for those Pokemon to use in battle, with information such as power, accuracy, and typing. They can be joined together through the mutually shared 'type' attribute. Below are links to the dataset:
# https://www.kaggle.com/datasets/rounakbanik/pokemon
# https://www.kaggle.com/datasets/thiagoamancio/full-pokemons-and-moves-datasets

# ==================================================
# Task 2: Load the datasets into Pandas DataFrames. Display the first 5 rows of each dataset, with the column names. Identify which column will be used for joining.
# ==================================================

import numpy as np
import pandas as pd
#import os
import sys

sys.stdout = open("task-2-output.txt", "w", encoding="utf-8")

print("# ==================================================\n# Task 1: Download two datasets. Describe where they were sourced from, what they contain, and why they can be joined together.\n# ==================================================\n\n# The datasets were sourced from Kaggle, an open dataset platform, and contain two different tables of data pertaining to Pokemon. One of them contains all of the available Pokemon species in the mainline games, with information such as name, typing, abilities, and battle stats. The other contains the moves available for those Pokemon to use in battle, with information such as power, accuracy, and typing. They can be joined together through the mutually shared 'type' attribute.\nBelow are links to the dataset:\n# https://www.kaggle.com/datasets/rounakbanik/pokemon\n# https://www.kaggle.com/datasets/thiagoamancio/full-pokemons-and-moves-datasets")

#pd.set_option("display.max_columns", None)

#os.getcwd()

print("\n# ==================================================\n# Task 2: Load the datasets into Pandas DataFrames. Display the first 5 rows of each dataset, with the column names. Identify which column will be used for joining.\n# ==================================================")

dfSpecies = pd.read_csv(r"pokemon.csv")
dfMoves = pd.read_csv(r"metadata_pokemon_moves.csv")

#dfSpecies.drop(["abilities","against_bug","against_dark","against_dragon","against_electric","against_fairy","against_fight","against_fire","against_flying","against_ghost","against_grass","against_ground","against_ice","against_normal","against_poison","against_psychic","against_rock","against_steel","against_water",attack,base_total,defense,height_m,hp,name,pokedex_number,sp_attack,sp_defense,speed,type1,type2,weight_kg,generation,is_legendary], axis = 1, inplace = True)

dfSpecies.drop(["base_egg_steps","base_happiness","capture_rate","classfication","experience_growth","japanese_name","percentage_male","against_bug","against_dark","against_dragon","against_electric","against_fairy","against_fight","against_fire","against_flying","against_ghost","against_grass","against_ground","against_ice","against_normal","against_poison","against_psychic","against_rock","against_steel","against_water","base_total","generation","is_legendary","pokedex_number"], axis = 1, inplace = True)
dfMoves.drop(["id","generation","short_descripton","priority"], axis = 1, inplace = True)

dfSpecies["type2"] = dfSpecies["type2"].fillna("none")
dfMoves["type"] = dfMoves["type"].str.lower()

#print("spc", dfSpecies)
#print("moves", dfMoves)

topRowsSpecies = dfSpecies.head(5)
topRowsMoves = dfMoves.head(5)
speciesColumns = dfSpecies.columns
movesColumns = dfMoves.columns

print(f"\nFirst 5 rows of species table:\n{topRowsSpecies}\n\nFirst 5 rows of moves table:\n{topRowsMoves}\n\nColumn headings for species table:\n{speciesColumns}\n\nColumn headings for moves table:\n{movesColumns}\n")

# The columns that can be used for joining are the typing columns from the moves table and the two type columns in species. It would also be possible to manipulate the data slightly and make the 'type chart' section of the tables joinable. The use in joining at the type columns would be to identify what moves Pokemon can utilise to benefit from STAB (Same Type Attack bonus), a game mechanic whereby moves receive a 50% power boost if they share a type with the Pokemon using them.

print("# The columns that can be used for joining are the typing columns from the moves table and the two type columns in species. It would also be possible to manipulate the data slightly and make the 'type chart' section of the tables joinable. The use in joining at the type columns would be to identify what moves Pokemon can utilise to benefit from STAB (Same Type Attack bonus), a game mechanic whereby moves receive a 50% power boost if they share a type with the Pokemon using them.\n")

# ==================================================
# Task 3: Perform an inner join using a common column. Display the dataset.
# ==================================================

print("\n# ==================================================\n# Task 3: Perform an inner join using a common column. Display the dataset.\n# ==================================================\n")

"""import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '')

mycursor = mydb.cursor(buffered = True)
print(type(mycursor))

"""

joinDf = pd.merge(dfSpecies, dfMoves, how = "inner", left_on = "type1", right_on = "type")

#joinDf = pd.merge(dfSpecies, dfMoves, left_on = "type1", right_on = "type")

print("# ==================================================\n# Inner Join:\n# ==================================================\n", joinDf)

print("\n# When joining two dataframes via inner join, all of the records that have matching values within the parameters set will be included in the resulting dataframe. Conversely, if the records have no matching values, they will be excluded.")

print("\n# ==================================================\n# Task 5: Perform a full outer join on the selected datasets. Identify rows containing missing values (NaN).\n# ==================================================\n")

fJoinDf = pd.merge(dfSpecies, dfMoves, left_on="type1",right_on="type", how="outer")

print("\n# ==================================================\n# Outer Join:\n# ==================================================\n", fJoinDf)

nanDf = fJoinDf[fJoinDf.isna().any(axis = 1)]

print("\n# ==================================================\n# NaN rows:\n# ==================================================\n", nanDf)

print("Full outer joins return all records from both dataframes, which includes records that have missing values. There are a lot of records with NaN values in this dataset, which makes sense; some Pokemon moves do not have power or accuracy attributes, as they may be status inflicting moves, or bypass accuracy checks.")

print("\n# ==================================================\n# Task 6: Source two datasets with the same structure. Combine them using a union join. Remove duplicate records if necessary.\n# ==================================================\n")

print("\n# The dataset used for this task comes from basketball-reference, a subsite of the larger sports-reference network.\n# Links below:\n# https://www.basketball-reference.com/leagues/NBA_2026_per_game.html\n# https://www.basketball-reference.com/leagues/NBA_2011_per_game.html\n")

df2526 = pd.read_csv(r"25_26_nba.csv")
print(df2526)
df1011 = pd.read_csv(r"10_11_nba.csv")
print(df1011)
unionDf = pd.concat([df2526, df1011], ignore_index=True)
unionDf = unionDf.drop_duplicates(subset="Player")

print(unionDf)

print("\n# Rather than joining records via appending columns to the dataframe, union joins append rows to the end of the dataset, creating new records rather than changing the current records.\n\n# In real data analysis, this can be used for time series, or to compare records with the same data structure i.e. exam results across multiple schools across the country.\n")

print("\n# ==================================================\n# Task 7: Identify at least one data quality issue. Suggest one improvement to improve the dataset quality. Provide one simple insight gained from the joined data.\n# ==================================================\n")

print("\n# With the original Pokemon moves dataset being joined to the Pokemon species dataset in order to find viable STAB moves for each species, I only joined the data via the move type and the Pokemon's primary typing. Some pokemon have secondary types, which also receive STAB, so to improve the dataset I should find a way to join the moves if the secondary typing also matches the move type.\n# When we look over the joined dataset, we can see that every type has a wide variety of STAB moves to use. This indicates that the game has been well balanced in order to not provide any one particular type an advantage that could potentially limit the variety of strategies used by players.")

#joinDf.to_csv("joinTest.csv", mode = "a", index = True, header = False)
unionDf.to_csv("unionTest.csv", index = True, header = False)

sys.stdout.close()