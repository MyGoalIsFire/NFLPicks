import pandas as pd

data = pd.read_csv('D:/Dev/NFLtest/spread.csv')

del data['']
data
data.to_csv('D:/Dev/NFLpicks/spread.csv')

data = pd.read_csv('D:/Dev/NFLpicks/spread.csv')