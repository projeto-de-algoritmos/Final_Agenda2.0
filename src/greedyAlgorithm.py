from datetime import datetime
from datetime import timedelta
# scheduling to minimize lateness
# order by deadline - earliest deadline first


def interval_scheduling(events):
    events.sort(key=lambda x: x.deadline)
    # parse current date to YYYY-MM-DD format
    time = datetime.now()
    schedule = []

    # assign to event its start time and end time
    for event in events:
        event.set_start_time(time)
        # duration = event.get_duration()
        # print(type(duration))
        event.set_end_time(time + timedelta(days=event.get_duration()))
        schedule.append(event)
        time = event.get_end_time()
    return schedule
