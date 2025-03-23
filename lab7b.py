#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second.
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"

def sum_times(t1, t2):
    """Add two Time objects and return the sum with proper carry-over."""
    total_seconds = (t1.hour * 3600 + t1.minute * 60 + t1.second) + \
                    (t2.hour * 3600 + t2.minute * 60 + t2.second)
    
    new_hour = (total_seconds // 3600) % 24  # Ensuring it stays within 24-hour format
    new_minute = (total_seconds % 3600) // 60
    new_second = total_seconds % 60

    return Time(new_hour, new_minute, new_second)

def valid_time(t):
    """Check if the time object attributes are valid."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

def change_time(time, seconds):
    """Modify a Time object by adding or subtracting seconds, handling carry-over correctly."""
    time.second += seconds

    # Handle positive and negative values for seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # Handle positive and negative values for minutes
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    return None
