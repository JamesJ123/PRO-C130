import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["Star_name2"]
del df["Distance2"]
del df["Mass2"]
del df["Radius2"]

df.to_csv('cleaned.csv') 