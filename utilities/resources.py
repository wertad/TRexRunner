import os

# Ezzel a megolsással van egy aprócska gond:
# ha mondjuk c:\utilities\TRex\utilities mappát kap,
# akkor érvénytelen lesz az útvonal...
PROJECT_ROOT = os.path.dirname(__file__).replace("utilities", "")
RESOURCES_PATH = os.path.join(PROJECT_ROOT, "resources")


def get_resource_path(resource_name):
    full_path = os.path.join(RESOURCES_PATH, resource_name)
    assert os.path.exists(full_path), f"File does not exist: {full_path}"

    return full_path
