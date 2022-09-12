from datetime import datetime
from datetime import timedelta
# event class according to google calendar


class Event():
    # int: deadline
    # int: duration
    # str: name
    # str: description
    # str: start_time

    def __init__(self, deadline, duration, name, description="", start_time=datetime.now(), end_time=datetime.now()):
        self.deadline = deadline
        self.duration = duration
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "Event: " + self.name + "\n" + "Deadline: " + str(self.deadline) + "\n" + "Duration: " + str(self.duration) + "\n" + "Start time: " + str(self.start_time) + "\n" + "End time: " + str(self.end_time) + "\n" + "Description: " + self.description + "\n"

    # getters
    def get_deadline(self):
        return self.deadline

    def get_duration(self):
        return self.duration

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    # setters
    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_duration(self, duration):
        self.duration = duration

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time
    # methods

    # #duration is given in days
    # def calculate_end_time(self):
    #     # parse duration to sum
    #     self.end_time = self.start_time + timedelta(days=self.duration)
    #     return self.end_time
