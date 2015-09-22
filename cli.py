import requests
import click
import sys

import exceptions
from writer import get_writer

BASE_URL = "http://challengehuntapp.appspot.com/"

def get_contests_data():
  req = requests.get(BASE_URL)

  if req.status_code == requests.codes.ok:
    return req.json()
  else:
    click.secho("Couldn't get the data exiting...", fg="red", bold=True)
    sys.exit()


def active_contests(platform):
  contests_data = get_contests_data()
  writers.active_contests(contests_data["active"])
  

def upcoming_contests(platform):
  contests_data = get_contests_data()
  writers.upcoming_contests(contests_data["pending"])

def get_all_contests():
  contests_data = get_contests_data()
  writers.all_contests(contests_data)


@click.command()
@click.option('--active', is_flag=True, help="Shows all the active contests")
@click.option('--upcoming', is_flag=True, help="Shows all the upcoming contests")
@click.option('--platform', '-p', type=click.Choice(PLATFORM_IDS.keys()),
              help=("Choose the platform whose fixtures you want to see. "
                "See platform codes for more info"))
def main(active, upcoming, platform):
  """A CLI for actve and upcoming programming challenges from various platforms"""
  try:
    if active:
    	active_contests(platform)
      return

    if upcoming:
      upcoming_contests(platform)
      return

    get_all_contests()
  except IncorrectParametersException as e:
    click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
  main()
