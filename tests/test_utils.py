from os import path

PRESETS_DIR = path.join(path.dirname(__file__), 'presets')


def get_content(file):
    with open(path.join(PRESETS_DIR, file)) as f:
        return f.read()
