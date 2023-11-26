import pandas as pd

date_csv = 'https://gist.githubusercontent.com/adgedenkers/d649f2d74c2ecfa2b211c60c098db03d/raw/'
dates = pd.read_csv(date_csv, parse_dates=['date'])
dates['date'] = dates['date'].dt.date
dates['date'] = dates['date'].apply(str)