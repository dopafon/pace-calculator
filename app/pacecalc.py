from datetime import time
import datetime

def get_bikepace_by_time(distance_metres, target_time_seconds):
    kmh = distance_metres / target_time_seconds * 3.6
    return kmh
'''
def get_biketime_by_pace(pace_kmh, distance_metres):
    secs_per_km = 
    m_per_min = pace_kmh * distance_metres / 60
'''
def get_swimpace_by_time(distance_metres, target_time_seconds):
    """return pace as time string"""
    sec_per_100 = target_time_seconds / distance_metres * 100
    return str(convert_secs_to_time(sec_per_100))

def get_time_by_pace(pace_seconds, distance_metres):
    """returns str(time object)"""
    target_time_secs = pace_seconds * distance_metres / 100
    to = datetime.timedelta(seconds=int(target_time_secs))
    return str(to)

def get_secs_from_time(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def convert_secs_to_time(secs):
    """Get time from seconds int"""
    to = datetime.timedelta(seconds=int(secs))
    return str(to)

def create_swimsplits(time_seconds, distance_metres):
    """Return Dict of swimsplit times as time strings per 100"""
    swimsplits = {}
    pace_secs = time_seconds / distance_metres * 100
    t = pace_secs
    split = 100
    while t <= time_seconds:
        #swimsplits.append(convert_secs_to_time(t))
        swimsplits[split] = convert_secs_to_time(t)
        t += pace_secs
        split += 100
    return swimsplits
