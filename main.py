import pandas as pd
import matplotlib.pyplot as pl
import numpy as np

tempo_dict = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

dffd = pd.DataFrame.from_dict (tempo_dict)

df = pd.read_csv('pokemon_data.csv')
print (df.describe())


