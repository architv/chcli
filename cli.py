import requests
import click

import exceptions

BASE_URL = ""

def get_contests_data():
  req = requests.get(BASE_URL)

  if req.status_code == requests.codes.ok:
    return req.json()
  
  return None

def print_active_contests(platform):
  contests_data = get_contests_data()

  if contests_data:

    for active_contest in contests_data["active"]:
      pass
      
    
  else:
    click.secho("Data not available at the moment.", fg="red", bold=True)
	

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
    	get_active_contests(platform)

    get_all_contests()
  except IncorrectParametersException as e:
    click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
  main()