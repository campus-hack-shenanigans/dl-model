import pandas as pd
path_shakespeare  = "/home/kacper/Desktop/Hackathons/CampusHack2019/PoetRNN/data/shakespeare_data.csv"
path_kanye = "/home/kacper/Desktop/Hackathons/CampusHack2019/PoetRNN/data/kanye3.csv"

# import csv files
shakespeare_df = pd.read_csv(path_shakespeare, sep='\n') 
kanye_df = pd.read_csv(path_kanye)

merged_df  = pd.concat([shakespeare_df, kanye_df])
merged_df  = merged_df.sample(frac=1).reset_index(drop=True)

merged_df.to_csv("./data/shakespeare_eminem_combo", index = False)