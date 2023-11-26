'''
file:  generate_date_dimension.py
version: 2.1
project: fz
author: adge denkers / @adgedenkers
created: 2022-04-21
updated: 2023-11-06
'''

import pandas as pd
import requests
from datetime import date, timedelta

# Function to determine day suffix
def day_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        return "th"
    else:
        return ["st", "nd", "rd"][day % 10 - 1]

# Fetch the school days off JSON data from the provided URL
# url = 'http://denkers.co/2023_school_days_off.json'
# response = requests.get(url)
# if response.status_code != 200:
#     raise Exception(f"Failed to retrieve data: HTTP {response.status_code}")
# school_days_off_json = response.json()

school_days_off_list = [
    (date(2023, 11, 10), "Veterans Day (Observed)", "Full Day"),
    (date(2023, 11, 22), "Thanksgiving Recess", "Full Day"),
    (date(2023, 11, 23), "Thanksgiving Day", "Full Day"),
    (date(2023, 11, 24), "Thanksgiving Recess", "Full Day"),
    (date(2023, 12,  1), "Parent/Teacher Conferences", "Half Day"),
    (date(2023, 12,  4), "Parent/Teacher Conferences", "Half Day"),
    (date(2023, 12, 25), "Christmas Day", "Full Day"),
    (date(2023, 12, 26), "Winter Recess", "Full Day"),
    (date(2023, 12, 27), "Winter Recess", "Full Day"),
    (date(2023, 12, 28), "Winter Recess", "Full Day"),
    (date(2023, 12, 29), "Winter Recess", "Full Day"),
    (date(2024,  1,  1), "New Year's Day", "Full Day"),
    (date(2024,  1, 15), "Martin Luther King, Jr. Day", "Full Day"),
    (date(2024,  2, 19), "February Break", "Full Day"),
    (date(2024,  2, 20), "February Break", "Full Day"),
    (date(2024,  2, 21), "February Break", "Full Day"),
    (date(2024,  2, 22), "February Break", "Full Day"),
    (date(2024,  2, 23), "February Break", "Full Day"),
    (date(2024,  3, 18), "Vacation Day", "Full Day"),
    (date(2024,  3, 22), "Parent/Teacher Conferences", "Half Day"),
    (date(2024,  3, 25), "Parent/Teacher Conferences", "Half Day"),
    (date(2024,  3, 29), "Good Friday", "Full Day"),
    (date(2024,  4,  1), "Spring Recess", "Full Day"),
    (date(2024,  4,  2), "Spring Recess", "Full Day"),
    (date(2024,  4,  3), "Spring Recess", "Full Day"),
    (date(2024,  4,  4), "Spring Recess", "Full Day"),
    (date(2024,  4,  5), "Spring Recess", "Full Day"),
    (date(2024,  5, 28), "Memorial Day", "Full Day"),
    (date(2024,  6, 19), "Juneteenth", "Full Day"),
]

# Convert list of tuples to a DataFrame for easier processing
school_days_off_df = pd.DataFrame(school_days_off_list, columns=['date', 'event', 'duration'])


# Convert JSON object to a set of dates for easier lookup
school_days_off = school_days_off_df['date'].to_list()

# Define the date range for the DataFrame
start_date = date(2023, 1, 1)
end_date = date(2070, 12, 31)

# Prepare initial values for the pay period and A/B school day
pp_start_date = date(2023, 1, 1)
pp_counter = 1
ab_day_flag = 'A'

# Initialize the DataFrame
date_list = []

# Iterate through the dates
for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days + 1)):
    dow_num = single_date.isoweekday()
    weekend = 1 if dow_num in [6, 7] else 0
    suffix = day_suffix(single_date.day)
    woy = single_date.isocalendar()[1]

    ny = single_date.timetuple().tm_yday
    
    if ny == 1:
        print(single_date.year)
    
    # Pay period logic
    if single_date >= pp_start_date + timedelta(days=14):
        pp_start_date += timedelta(days=14)
        pp_counter += 1
    if single_date.year != pp_start_date.year:
        pp_start_date = date(single_date.year, 1, 1)
        pp_counter = 1
    pp = f"{str(single_date.year)[2:]}-{str(pp_counter).zfill(2)}"
    
    # School A/B day logic
    if single_date >= date(2023, 9, 7) and single_date.weekday() < 5 and not weekend and single_date not in school_days_off:
        school_day = 1
        school_ab_day = ab_day_flag
        ab_day_flag = 'A' if ab_day_flag == 'B' else 'B'
    else:
        school_day = 0
        school_ab_day = ''
    
    # Adding the date information to the list
    date_list.append({
        "date": single_date,
        "day": single_date.day,
        "suffix": suffix,
        "dow_name": single_date.strftime("%A"),
        "dow_num": dow_num,
        "doy": single_date.timetuple().tm_yday,
        "weekend": weekend,
        "woy": single_date.isocalendar()[1],
        "fow": single_date - timedelta(days=single_date.weekday()),
        "low": single_date + timedelta(days=(6-single_date.weekday())),
        "wom": (single_date.day - 1) // 7 + 1,
        "month": single_date.month,
        "moy_name": single_date.strftime("%B"),
        "fom": single_date.replace(day=1),
        "lom": (single_date.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1),
        "gov_quarter": (single_date.month - 1) // 3 + 1,
        "year": single_date.year,
        "cy": single_date.year,
        "fy": single_date.year if single_date.month >= 10 else single_date.year - 1,
        "leap_year": int(single_date.year % 4 == 0 and (single_date.year % 100 != 0 or single_date.year % 400 == 0)),
        "53_weeks": int(woy == 53),
        "disp_date": single_date.strftime("%Y-%m-%d"),
        "disp_mm_yyyy": single_date.strftime("%m/%Y"),
        "disp_mm_dd_yyyy": single_date.strftime("%m/%d/%Y"),
        "disp_date_suffix": single_date.strftime("%Y%m%d"),
        "ppid": (single_date.year - start_date.year) * 26 + pp_counter,
        "pp": pp,
        "ppy": int(pp.split('-')[0]),
        "ppn": int(pp.split('-')[1]),
        "ppw": (single_date - pp_start_date).days // 7 + 1,
        "ppd": (single_date - pp_start_date).days % 14 + 1,
        "pp_start": pp_start_date,
        "pp_end": pp_start_date + timedelta(days=13),
        "pay_day": 0,  # Set your own logic for pay_day
        "school_open": 1 if single_date >= date(2023, 9, 7) and single_date < date(2024, 7, 1) else 0,
        "school_day": school_day,
        "school_ab_day": school_ab_day
    })

# Create the DataFrame
dim_date_df = pd.DataFrame(date_list)

dim_date_df.to_csv('dates.csv', index=False)
