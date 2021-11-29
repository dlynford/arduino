import pandas as pd
temps = pd.read_csv("kitchen_temp.csv")
print(temps)
print(temps.describe())
print(temps.info())
