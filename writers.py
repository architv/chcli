import json

def get_writer(output_format='stdout', output_file=None):
    return globals()[output_format.capitalize()](output_file)

    