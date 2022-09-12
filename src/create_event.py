from datetime import datetime, timedelta
from cal_setup import get_calendar_service
# import get_calendar_service


def create_event(name, start_time, end_time, description):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    # d = datetime.now().date()
    # tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    # start = tomorrow.isoformat()
    # end = (tomorrow + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": name,
                                               "description": description,
                                               "start": {"dateTime": start_time.isoformat(), "timeZone": 'Brazil/East'},
                                               "end": {"dateTime": end_time.isoformat(), "timeZone": 'Brazil/East'},
                                           }
                                           ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])



