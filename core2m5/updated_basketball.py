# Imports for Google API and Authentication
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Standard Library Imports
import os.path
import pickle
import datetime
import pytz
from datetime import datetime, timedelta

# Configuration Variables
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CLIENT_SECRET_FILE = "/Users/adge/.secret/client_secret_903345666419-d3d348vf0094huo3a7vsj6m3vv8g26ul.apps.googleusercontent.com.json"
TOKEN_FILE = 'token.pickle'
CALENDAR_ID = 'c_008ad5bc717d02d0b89445f38b11340a45c4ea6d0f33c77fe888b04e37452ffc@group.calendar.google.com'  # Replace with your actual calendar ID
KEYWORD = 'boys'
TIMEZONE = pytz.timezone('America/New_York')
TIMEFRAME = 'this_week'  # Options: 'today', 'this_week', 'next_week', 'this_month', 'next_month'

def get_calendar_service():
    """
    Authenticate and return a service object to interact with Google Calendar API.

    Returns:
        service: Authorized Google Calendar service object.
    """
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def get_time_range(timeframe):
    """
    Determine the start and end time based on the specified timeframe.

    Args:
        timeframe (str): The timeframe to get events for ('today', 'this_week', 'next_week').

    Returns:
        tuple: Start and end time in ISO format.
    """
    now = datetime.now(TIMEZONE)
    if timeframe == 'today':
        start_time = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = now.replace(hour=23, minute=59, second=59, microsecond=999999)
    elif timeframe == 'this_week':
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        start_time = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = end_of_week.replace(hour=23, minute=59, second=59, microsecond=999999)
    elif timeframe == 'next_week':
        start_of_next_week = now + timedelta(days=-now.weekday(), weeks=1)
        end_of_next_week = start_of_next_week + timedelta(days=6)
        start_time = start_of_next_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = end_of_next_week.replace(hour=23, minute=59, second=59, microsecond=999999)
    else:
        raise ValueError("Invalid timeframe specified")

    return start_time.isoformat(), end_time.isoformat()

def list_filtered_events(calendar_id, keyword, timeframe):
    """
    List and print events from a Google Calendar filtered by a keyword and within a specified timeframe.

    Args:
        calendar_id (str): The ID of the Google Calendar.
        keyword (str): Keyword to filter events by their summary.
        timeframe (str): The timeframe to get events for ('today', 'this_week', 'next_week').
    """
    service = get_calendar_service()
    start_time, end_time = get_time_range(timeframe)

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=start_time,
        timeMax=end_time,
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print(f'No upcoming events found for {timeframe}.')
        return

    for event in events:
        summary = event.get('summary', '').lower()
        if keyword.lower() in summary:
            start, end = event['start'].get('dateTime'), event['end'].get('dateTime')
            print_event_details(start, end, event['summary'])

def list_todays_events(calendar_id, keyword):
    """
    List and print events today, from a Google Calendar filtered by a keyword.
    
    Args:
        calendar_id (str): The ID of the Google Calendar.
        keyword (str): Keyword to filter events by their summary.
    """
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'  # Current time in UTC
    end_of_today = (datetime.utcnow() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'  # End of today in UTC

    events_result = service.events().list(calendarId=calendar_id,
                                          timeMin=now,
                                          timeMax=end_of_today,
                                          maxResults=50,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    for event in events:
        summary = event.get('summary', '').lower()
        if summary.startswith(keyword.lower()):
            start, end = event['start'].get('dateTime'), event['end'].get('dateTime')
            print_event_details(start, end, event['summary'])

def list_filtered_events(calendar_id, keyword):
    """
    List and print events from a Google Calendar filtered by a keyword.

    Args:
        calendar_id (str): The ID of the Google Calendar.
        keyword (str): Keyword to filter events by their summary.
    """
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'  # Current time in UTC

    events_result = service.events().list(calendarId=calendar_id,
                                          timeMin=now,
                                          maxResults=25,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    for event in events:
        summary = event.get('summary', '').lower()
        if summary.startswith(keyword.lower()):
            start, end = event['start'].get('dateTime'), event['end'].get('dateTime')
            print_event_details(start, end, event['summary'])

def print_event_details(start, end, summary):
    """
    Print the details of an event.

    Args:
        start (str): Start datetime of the event in ISO format.
        end (str): End datetime of the event in ISO format.
        summary (str): Summary of the event.
    """
    parsed_start = datetime.fromisoformat(start).astimezone(TIMEZONE) if start else None
    parsed_end = datetime.fromisoformat(end).astimezone(TIMEZONE) if end else None
    formatted_start = parsed_start.strftime("%B %d, %Y %I:%M %p") if parsed_start else "Unknown start time"
    formatted_end = parsed_end.strftime("%I:%M %p") if parsed_end else "Unknown end time"
    print(f"{formatted_start} to {formatted_end}, {summary}")

def main():
    """
    Main function to execute the script logic.
    """
    if TIMEFRAME == 'today':
        list_todays_events(CALENDAR_ID, KEYWORD)
    else:
        list_filtered_events(CALENDAR_ID, KEYWORD)

if __name__ == "__main__":
    main()