#!/usr/bin/env python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        """Initialize a Time object with hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Return a string representation for the object self.'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''Return a string representation for the object self.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Add two Time objects using the + operator."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def time_to_sec(self):
        """Convert time to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def format_time(self):
        """Return time as a formatted string (HH:MM:SS)."""
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def sum_times(self, other):
        """Add two Time objects and return a new Time object."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify time by adding seconds, adjusting overflow."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def valid_time(self):
        """Check if the time is valid."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

def sec_to_time(seconds):
    """Convert total seconds to a Time object."""
    seconds %= 86400  # Keep within a day's range
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return Time(hour, minute, second)
