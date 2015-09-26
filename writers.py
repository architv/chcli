import json

import click

from datetime import datetime, timedelta
from time import strptime

def colors():
  """Creates an enum for colors"""
  enums = dict(
    TIME_LEFT="red",
    CONTEST_NAME="yellow",
    HOST="green",
    MISC="blue",
  )

  return type('Enum', (), enums)


def format_date(date_object):
  """Formats the date and returns the datetime object"""
  date_time = date_object.split("+")
  return datetime.strptime(str(date_time[0]), "%Y-%m-%dT%H:%M:%S")


def write_active_contests(contests):
  """Prints the contests in a pretty way"""
  # click.secho("%-6s  %-30s    %-10s    %-10s    %-10s" % ("NO.", "NAME", "TIME LEFT", "DURATION", "PLATFORM"))

  for index, contest in enumerate(contests):
    time_left = format_date(contest["end"]) - datetime.utcnow()
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_left_string = ""

    if time_left.days > 0: 
      time_left_string = "{0} days {1} hours".format(time_left.days, hours)
    elif hours > 0:
      time_left_string = "{0} hours {1} minutes".format(hours, minutes)
    else:
      time_left_string = "{0} minutes".format(minutes)

    click.echo()
    click.secho("%-3s" % str(index+1), nl=False, bold=True)
    click.secho("  %-50s" %
                (contest["contest_name"]), nl=False, fg=colors().CONTEST_NAME, bold=True)
    click.secho("    %-20s" % time_left_string, nl=False, fg=colors().TIME_LEFT, bold=True)
    click.secho("    %-11s" %
                 str(contest["duration"]), nl=False, bold=True)
    click.secho("    %-15s" % contest["host_name"], fg=colors().HOST, bold=True)
