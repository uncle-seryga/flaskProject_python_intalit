import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '73anh38-d3NR-d38dHd8BdN'

