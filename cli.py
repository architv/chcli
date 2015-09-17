import requests
import click

BASE_URL = "http://challengehuntapp.appspot.com/"

def get_active_contests():
  pass
	

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
    	get_active_contests(platforms)

    get_all_contests()
  except IncorrectParametersException as e:
    click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
  main()