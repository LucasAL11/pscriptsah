

def config_reader(path):
    """
    Reads a configuration file line by line and returns a list of strings
    with leading and trailing whitespace removed.

    :param path: The path to the configuration file to be read
    :return: A list of strings with leading and trailing whitespace removed
    """
    with open(path) as file:
        while line := file.readline():
            return [line.rstrip() for line in file]
