from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import os.path
import pickle
import datetime
import pytz

from datetime import datetime, date, time, timedelta

local_tz = pytz.timezone('America/New_York')
local_now = datetime.now(local_tz)
utc_now = local_now.astimezone(pytz.utc)
dt = utc_now.strftime("%Y-%m-%d")


# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

goog = "/Users/adge/.secret/client_secret_903345666419-d3d348vf0094huo3a7vsj6m3vv8g26ul.apps.googleusercontent.com.json"

def convert__to_zulu():
    dt = date.split('/')
    month = int(dt[0])
    day = int(dt[1])
    year = int(dt[2])
    return_obj = datetime(year, month, day)
    return return_obj

def convert__to_zulu_set_time(time):
    # convert to zulu time, by providing a local time
    t = time.split(':')
    hour = int(t[0])
    minute = int(t[1])
    dt = date.split('/')
    month = int(dt[0])
    day = int(dt[1])
    year = int(dt[2])
    return_obj = datetime(year, month, day, 23, 59, 59.999999)
    return return_obj

def get_calendar_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                goog, SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def show__todays_basketball_info():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    events_result = service.events().list(calendarId=calendar_id,
                                          timeMin=now,
                                          maxResults=25, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])


def list_filtered_events(calendar_id, keyword):
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    events_result = service.events().list(calendarId=calendar_id,
                                          timeMin=now,
                                          maxResults=25, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    for event in events:
        summary = event.get('summary', '').lower()
        if summary.startswith(keyword.lower()):
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))

            parsed_start_datetime = datetime.fromisoformat(start)
            parsed_end_datetime = datetime.fromisoformat(end)

            formatted_start_time = parsed_start_datetime.strftime("%B %d, %Y %I:%M %p")
            formatted_end_time = parsed_end_datetime.strftime("%I:%M %p")

            print(f"{formatted_start_time} to {formatted_end_time}, {event['summary']}")


# Replace 'your_calendar_id' with the actual calendar ID
calendar_id = 'c_008ad5bc717d02d0b89445f38b11340a45c4ea6d0f33c77fe888b04e37452ffc@group.calendar.google.com'
keyword = 'boys'
list_filtered_events(calendar_id, keyword)
