import datetime
import pandas as pd

date_csv = 'https://gist.githubusercontent.com/adgedenkers/d649f2d74c2ecfa2b211c60c098db03d/raw/'
dates = pd.read_csv(date_csv, parse_dates=['date'])
dates['date'] = dates['date'].dt.date
dates['date'] = dates['date'].apply(str)


def clean_date_column(df, date_column):
    df[date_column] = df[date_column].str.replace('T00:00:00.000Z', '')
    df[date_column] = df[date_column].str.replace('T00:00:00.000', '')
    df[date_column] = df[date_column].str.replace('T00:00:00', '')
    df[date_column] = df[date_column].str.replace('T00:00', '')
    df[date_column] = df[date_column].str.replace('T', ' ')
    df[date_column] = df[date_column].str.replace('Z', '')
    df[date_column] = df[date_column].str.replace('1/1/1900', '')
    df[date_column] = df[date_column].dt.date
    df[date_column] = df[date_column].apply(str)
    return df