

def config_reader(path):
    with open(path) as file:
        while line := file.readline():
            return [line.rstrip() for line in file]

r''