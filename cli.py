import requests
import click
import sys

from local_exceptions import IncorrectParametersException
import writers
from platformids import platforms as contest_platforms
from utilities import time_difference

BASE_URL = "http://challengehuntapp.appspot.com/"
PLATFORM_IDS = contest_platforms

def check_platforms(platforms):

  if len(platforms) > 0:
    if all(platform in PLATFORM_IDS for platform in platforms):
      return True
    else:
      return False
  
  return True


def get_contests_data():
  req = requests.get(BASE_URL)

  if req.status_code == requests.codes.ok:
    return req.json()
  else:
    click.secho("Couldn't get the data", fg="red", bold=True)
    click.secho("Exiting...", fg="red", bold=True)
    sys.exit()


def active_contests(platforms):
  """Gets all the active contests based on time and platforms"""
  contests_data = get_contests_data()
  platform_filter = [PLATFORM_IDS[x] for x in platforms]

  if platforms:
    active_challenges = [contest for contest in contests_data["active"] if contest["host_name"] in platform_filter]
  else:
    active_challenges = contests_data["active"]

  writers.write_contests(active_challenges, "active")
  

def upcoming_contests(platforms, time):
  """Gets all the upcoming contests based on time and platforms"""
  contests_data = get_contests_data()
  platform_filter = [PLATFORM_IDS[x] for x in platforms]

  if platforms:
    upcoming_challenges = [contest for contest in contests_data["pending"] if contest["host_name"] in platform_filter 
    and time_difference(contest["start"]).days <= time]
  else:
    upcoming_challenges = [contest for contest in contests_data["pending"] 
    if time_difference(contest["start"]).days <= time]

  writers.write_contests(upcoming_challenges, "upcoming")


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
  writers.write_contests(hiring_challenges, "hiring")


def short_contests():
  """Gets all the short contests(less than or equal to 4 hours of duration)"""
  contests_data = get_contests_data()
  active_contests = contests_data["active"]
  upcoming_contests = contests_data["pending"]
  get_challenge_duration = lambda x : int(x.split(":")[0]) if "days" not in x else float("inf")
  short_contests = [contest for contest in active_contests
    if get_challenge_duration(contest["duration"]) <= 4]
  short_contests += [contest for contest in upcoming_contests
    if get_challenge_duration(contest["duration"]) <= 4]
  writers.write_contests(short_contests, "short")


def get_all_contests():
  contests_data = get_contests_data()
  # writers.all_contests(contests_data)


@click.command()
@click.option('--active', is_flag=True, help="Shows all the active contests")
@click.option('--upcoming', is_flag=True, help="Shows all the upcoming contests")
@click.option('--hiring', is_flag=True, help="Shows all the hiring contests")
@click.option('--short', is_flag=True, help="Shows all the short contests")
@click.option('--platforms', '-p', multiple=True,
  help=("Choose the platform whose fixtures you want to see. "
                "See platform codes for more info"))
@click.option('--time', '-t', default=6,
              help="The number of days in the past for which you want to see the contests")
def main(active, upcoming, hiring, short, platforms, time):
  """A CLI for actve and upcoming programming challenges from various platforms"""

  if not check_platforms(platforms):
    raise IncorrectParametersException('Invlaid code for platform. Please check the platform ids')

  try:
    if active:
      active_contests(platforms)
      return

    if upcoming:
      upcoming_contests(platforms, time)
      return

    if hiring:
      hiring_contests()
      return

    if short:
      short_contests()
      return

    get_all_contests()
  except IncorrectParametersException as e:
    click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
  main()
