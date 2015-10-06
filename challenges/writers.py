import json

import click

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


def challenge():
  """Creates an enum for contest type"""
  enums = dict(
    ACTIVE="active",
    UPCOMING="upcoming",
    HIRING="hiring",
    ALL="all",
    SHORT="short",
  )

  return type('Enum', (), enums)


def write_contests(contests, contest_type):
  """Prints the contests based on the parameters passed"""
  write_contest_header(contest_type)

  for index, contest in enumerate(contests):

    time_diff_string = get_time_string(contest, contest_type)
    contest_name = contest["contest_name"].encode('utf-8')

    click.echo()
    click.secho("%-3s" % str(index+1), nl=False, bold=True)
    click.secho("  %-50s" %
                contest_name, nl=False, fg=colors().CONTEST_NAME, bold=True)
    click.secho("    %-20s" % time_diff_string, nl=False, fg=colors().TIME_TO_START, bold=True)
    click.secho("    %-11s" %
                 str(contest["duration"]), nl=False, bold=True)
    click.secho("    %-15s" % contest["host_name"], fg=colors().HOST, bold=True)


def get_time_string(contest, contest_type):
  """Return a string with time for the contest to begin/end"""

  if contest_type == challenge().ACTIVE:
    time_diff = time_difference(contest["end"])
  elif contest_type == challenge().UPCOMING:
    time_diff = time_difference(contest["start"])
  elif contest_type in [challenge().HIRING, challenge().SHORT, challenge().ALL]:
    try:
      time_diff = time_difference(contest["start"])
    except:
      time_diff = time_difference(contest["end"])
  time_diff_string = ""

  if time_diff.days > 0: 
    time_diff_string = "{0} days {1} hours".format(time_diff.days, time_diff.hours)
  elif time_diff.hours > 0:
    time_diff_string = "{0} hours {1} minutes".format(time_diff.hours, time_diff.minutes)
  else:
    time_diff_string = "{0} minutes".format(time_diff.minutes)
  return time_diff_string


def write_contest_header(contest_type):
  """Prints the header for the type of contest"""
  if contest_type == challenge().ACTIVE:
    click.secho("%-3s  %-50s    %-20s    %-11s    %-15s" % 
    ("NO.", "NAME", "ENDS IN", "DURATION", "PLATFORM"))
  elif contest_type == challenge().UPCOMING:
    click.secho("%-3s  %-50s    %-20s    %-11s    %-15s" % 
    ("NO.", "NAME", "STARTS IN", "DURATION", "PLATFORM"))
  elif contest_type in [challenge().HIRING, challenge().SHORT, challenge().ALL]:
    click.secho("%-3s  %-50s    %-20s    %-11s    %-15s" % 
    ("NO.", "NAME", "STARTS/ENDS IN", "DURATION", "PLATFORM"))    
