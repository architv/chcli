from datetime import datetime, timedelta
from time import strptime

from collections import namedtuple

def format_date(date_object):
  """Formats the date and returns the datetime object"""
  # date_time = date_object.split("+")
  return datetime.strptime(str(date_object), "%Y-%m-%dT%H:%M:%S")


def time_difference(target_time):
  """Calculate the difference between the current time and the given time"""
  TimeDiff = namedtuple("TimeDiff", ["days", "hours", "minutes", "seconds"])
  time_diff = format_date(target_time) - datetime.utcnow()
  hours, remainder = divmod(time_diff.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return TimeDiff(days=time_diff.days, hours=hours, minutes=minutes, seconds=seconds)
