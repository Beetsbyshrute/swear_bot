DATABASE = {}


def fetch_value(key):
  if key in DATABASE:
    return DATABASE[key]
  else:
    return None


def set_value(key, value):
  DATABASE[key] = value
