import sys
import webbrowser

import requests
import click

from local_exceptions import IncorrectParametersException

import writers

from platformids import platforms as contest_platforms
from utilities import time_difference

BASE_URL = "http://challengehuntapp.appspot.com/v2"
PLATFORM_IDS = contest_platforms

def check_platforms(platforms):
  """Checks if the platforms have a valid platform code"""
  if len(platforms) > 0:
    return all(platform in PLATFORM_IDS for platform in platforms)
  return True


def get_contests_data():
  """Gets all the data for all the contests"""
  req = requests.get(BASE_URL)

  if req.status_code == requests.codes.ok:
    return req.json()
  else:
    click.secho("Couldn't get the data", fg="red", bold=True)
    click.secho("Exiting...", fg="red", bold=True)
    sys.exit()

def get_platform_filter(platforms):
    if platforms:
        platform_filter = [PLATFORM_IDS[platform] for platform in platforms]
    else:
        platform_filter = PLATFORM_IDS.values()
    return platform_filter

def active_contests(platforms):
  """Gets all the active contests based on time and platforms"""
  contests_data = get_contests_data()
  platform_filter = get_platform_filter(platforms)

  active_challenges = [contest for contest in contests_data["active"] if contest["host_name"] in platform_filter]

  return active_challenges
  

def upcoming_contests(platforms, time):
  """Gets all the upcoming contests based on time and platforms"""
  contests_data = get_contests_data()
  platform_filter = get_platform_filter(platforms)

  upcoming_challenges = [contest for contest in contests_data["pending"] if contest["host_name"] in platform_filter 
    and time_difference(contest["start"]).days <= time]

  return upcoming_challenges


def hiring_contests():
  """Gets all the hiring challenges from all the availbale platforms"""
  contests_data = get_contests_data()
  active_contests = contests_data["active"]
  upcoming_contests = contests_data["pending"]
  get_challenge_name = lambda x : x.lower().split()
  hiring_challenges = [contest for contest in active_contests
    if "hiring" in get_challenge_name(contest["contest_name"])]
  hiring_challenges += [contest for contest in upcoming_contests
    if "hiring" in get_challenge_name(contest["contest_name"])]
  return hiring_challenges


def short_contests(platforms):
  """Gets all the short contests(less than or equal to 4 hours of duration)"""
  contests_data = get_contests_data()
  active_contests = contests_data["active"]
  upcoming_contests = contests_data["pending"]

  platform_filter = get_platform_filter(platforms)
  get_challenge_duration = lambda x : int(x.split(":")[0]) if "days" not in x else float("inf")
  short_contests = [contest for contest in active_contests
    if get_challenge_duration(contest["duration"]) <= 4 and contest["host_name"] in platform_filter]
  short_contests += [contest for contest in upcoming_contests
    if get_challenge_duration(contest["duration"]) <= 4 and contest["host_name"] in platform_filter]
  return short_contests


def get_all_contests(platforms, time):
  """Gets all the contests and writes it to standard output"""
  contests_data = get_contests_data()
  active_contests = contests_data["active"]
  upcoming_contests = contests_data["pending"]

  platform_filter = get_platform_filter(platforms)

  contests_data = [contest for contest in active_contests 
  if contest["host_name"] in platform_filter]
  contests_data += [contest for contest in upcoming_contests 
  if contest["host_name"] in platform_filter and time_difference(contest["start"]).days <= time]
  return contests_data


@click.command()
@click.option('--active', is_flag=True, help="Shows all the active contests")
@click.option('--upcoming', is_flag=True, help="Shows all the upcoming contests")
@click.option('--hiring', is_flag=True, help="Shows all the hiring contests")
@click.option('--short', is_flag=True, help="Shows all the short contests")
@click.option('--platforms', '-p', multiple=True,
              help=("Choose the platform whose contests you want to see. "
                    "See platform codes for more info"))
@click.argument('goto', nargs=1, required=False, type=click.INT)
@click.option('--time', '-t', default=6,
              help="The number of days in the past for which you want to see the contests")
def main(active, upcoming, hiring, short, goto, platforms, time):
  """A CLI for active and upcoming programming challenges from various platforms"""

  if not check_platforms(platforms):
    raise IncorrectParametersException('Invlaid code for platform. Please check the platform ids')

  try:
    if active:
      active_challenges = active_contests(platforms)
      if goto:
        webbrowser.open(active_challenges[goto - 1]["contest_url"], new=2)
      else:
        writers.write_contests(active_challenges, "active")
      return

    if upcoming:
      upcoming_challenges = upcoming_contests(platforms, time)
      if goto:
        goto = int(goto)
        webbrowser.open(upcoming_challenges[goto - 1]["contest_url"], new=2)
      else:
        writers.write_contests(upcoming_challenges, "upcoming")
      return

    if hiring:
      hiring_challenges = hiring_contests()
      if goto:
        webbrowser.open(hiring_challenges[goto - 1]["contest_url"], new=2)
      else:
        writers.write_contests(hiring_challenges, "hiring")
      return

    if short:
      short_challenges = short_contests(platforms)
      if goto:
        goto = int(goto)
        webbrowser.open(short_challenges[goto - 1]["contest_url"], new=2)
      else:
        writers.write_contests(short_challenges, "short")
      return

    all_contests = get_all_contests(platforms, time)
    if goto:
      webbrowser.open(all_contests[goto - 1]["contest_url"], new=2)
    else:
      writers.write_contests(all_contests, "all")
  except IncorrectParametersException as e:
    click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
  main()
