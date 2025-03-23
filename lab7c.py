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

def time_to_sec(t):
    """Convert a Time object to total seconds."""
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert total seconds into a Time object."""
    hours = (seconds // 3600) % 24
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return Time(hours, minutes, seconds)

def sum_times(t1, t2):
    """Add two Time objects using seconds conversion."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify a Time object by adding or subtracting seconds using conversion functions."""
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)

    # Update the original object
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

    return None
