import yaml
import time


def timetag(timespec='days'):
    """


    Args:
        timespec:
            - days: YYYY-MM-DD (default)
            - hours: YYYY-MM-DDTHH
            - minutes: YYYY-MM-DDTHH:MM
            - seconds: YYYY-MM-DDTHH:MM:SS

    Returns: time tag (string)

    """

    if timespec == 'days':
        return datetime.datetime.isoformat(datetime.datetime.now()).split('T')[0]
    else:
        return datetime.datetime.isoformat(datetime.datetime.now(), timespec='seconds')

def load_parameters(filename):
    """

    Args:
        filename: name of file to save parameters e.g. parameters.txt

    Returns:

    """
    with open(filename) as f:
        parameters = yaml.load(f, Loader=yaml.FullLoader)

    return parameters

def save_parameters(filename, parameters):
    """

    Args:
        filename: name of file to save parameters e.g. parameters.txt
        parameters: parameters to be save - dictionary

    Returns: parameters dictionary

    """

    with open(filename, "w") as file:
        file.write(yaml.dump(parameters))
