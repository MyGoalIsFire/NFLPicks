import requests
import xml.etree.cElementTree as et
import pandas as pd
import matplotlib.pyplot as plt

game_year = []
game_week = []
game_id = []
game_time = []
home_team = []
home_score = []
visitor_team = []
visitor_score = []

for y in range(2011, 2020):
    for w in range(1, 18):
        url = 'http://www.nfl.com/ajax/scorestrip?season={}&seasonType=REG&week={}'.format(y, w)
        r = requests.get(url)
        root = et.fromstring(r.content)
        for child in root.iter('g'):
            game_year.append(y)
            game_week.append(w)
            game_id.append(child.attrib['eid'])
            game_time.append(child.attrib['t'])
            home_team.append(child.attrib['hnn'])
            home_score.append(child.attrib['hs'])
            visitor_team.append(child.attrib['vnn'])
            visitor_score.append(child.attrib['vs'])

df = pd.DataFrame({'Year': game_year, 'Week': game_week, 'Game ID': game_id, 'Game Time': game_time, 'Home': home_team, 'Home Score': home_score, 'Visitor': visitor_team, 'Visitor Score': visitor_score})
df = df[['Year','Week','Game ID','Game Time','Home','Home Score','Visitor','Visitor Score']]
df.to_csv(r'D:\Dev\NFLpicks\scores.csv')
df