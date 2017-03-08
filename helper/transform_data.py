## moves the data into a csv format from xlsx

import os
import pandas as pd

data_file = "../data/original_data/all.xls"

df = pd.read_excel(data_file)

# find country names
df = df.replace('Viet Nam', 'Vietnam')
df = df.replace('Timor-Leste', 'East Timor')
df = df.replace('United States of America', 'USA')
df = df.replace("Côte d'Ivoire", 'Ivory Coast')
df = df.replace("Venezuela (Bolivarian Republic of)", 'Venezuela')
df = df.replace("United Republic of Tanzania", 'Tanzania')
df = df.replace("Lao People's Democratic Republic", 'Laos')
df = df.replace("Democratic Republic of the Congo", 'Congo')
df = df.replace("Bolivia (Plurinational State of)", 'Bolivia')
df = df.replace("Republic of Korea", 'South Korea')
df = df.replace('United Kingdom of Great Britain and Northern Ireland', 'England')
df = df.replace('', '')

# clean opening and closing whitespaces
df = df.replace("\s$", "", regex=True)
df = df.replace("^\s", "", regex=True)

# print(df.target_country.unique().shape, df.target_country.unique())
# print("______")
# print(df.investor_country.unique().shape, df.investor_country.unique())

df.to_csv("../data/landmatrix/all.csv", sep="|")