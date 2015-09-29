import json

import click

from datetime import datetime, timedelta
from time import strptime
from utilities import time_difference

def colors():
  """Creates an enum for colors"""
  enums = dict(
    TIME_LEFT="red",
    CONTEST_NAME="yellow",
    HOST="green",
    MISC="blue",
    TIME_TO_START="green",
  )

  return type('Enum', (), enums)


def write_active_contests(contests):
  """Prints the contests in a pretty way"""
  click.secho("%-3s  %-50s    %-20s    %-11s    %-15s" % 
    ("NO.", "NAME", "ENDS IN", "DURATION", "PLATFORM"), fg="red")

  for index, contest in enumerate(contests):
    time_left = time_difference(contest["end"])
    time_end_string = ""

    if time_left.days > 0: 
      time_end_string = "{0} days {1} hours".format(time_left.days, time_left.hours)
    elif time_left.hours > 0:
      time_end_string = "{0} hours {1} minutes".format(time_left.hours, time_left.minutes)
    else:
      time_end_string = "{0} minutes".format(time_left.minutes)

    click.echo()
    click.secho("%-3s" % str(index+1), nl=False, bold=True)
    click.secho("  %-50s" %
                (contest["contest_name"]), nl=False, fg=colors().CONTEST_NAME, bold=True)
    click.secho("    %-20s" % time_end_string, nl=False, fg=colors().TIME_LEFT, bold=True)
    click.secho("    %-11s" %
                 str(contest["duration"]), nl=False, bold=True)
    click.secho("    %-15s" % contest["host_name"], fg=colors().HOST, bold=True)


def write_upcoming_contests(contests):
  """Prints the upcomign contests in a pretty way"""
  click.secho("%-3s  %-50s    %-20s    %-11s    %-15s" % 
    ("NO.", "NAME", "STARTS IN", "DURATION", "PLATFORM"))

  for index, contest in enumerate(contests):
    time_to_start = time_difference(contest["start"])
    time_start_string = ""

    if time_to_start.days > 0: 
      time_start_string = "{0} days {1} hours".format(time_to_start.days, time_to_start.hours)
    elif time_to_start.hours > 0:
      time_start_string = "{0} hours {1} minutes".format(time_to_start.hours, time_to_start.minutes)
    else:
      time_start_string = "{0} minutes".format(time_to_start.minutes)

    click.echo()
    click.secho("%-3s" % str(index+1), nl=False, bold=True)
    click.secho("  %-50s" %
                (contest["contest_name"]), nl=False, fg=colors().CONTEST_NAME, bold=True)
    click.secho("    %-20s" % time_start_string, nl=False, fg=colors().TIME_TO_START, bold=True)
    click.secho("    %-11s" %
                 str(contest["duration"]), nl=False, bold=True)
    click.secho("    %-15s" % contest["host_name"], fg=colors().HOST, bold=True)
