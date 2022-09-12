from userInterface import TelaAgenda
from event import Event
from greedyAlgorithm import interval_scheduling
from cal_setup import get_calendar_service
from create_event import create_event
from list_events import list_events
from list_calendars import list_calendars


if __name__ == "__main__":
    events = TelaAgenda.start()
    # print all events and their start and end time
    for event in events:
        print(event)

    # schedule events
    schedule = interval_scheduling(events)
    print("\n\n\n")
    print("Schedule:")
    for event in schedule:
        print(event)
    print("\n\n\n")

    # create events on google calendar
    for event in schedule:
        create_event(
            event.name, event.start_time, event.end_time, event.description)

    # list events on google calendar
    list_events()
