import logging as lg


class Logging():
    def __init__(self, file_name=None):
        if file_name:
            lg.basicConfig(filename=file_name, level=lg.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')

    def error(self, s):
        lg.error(s)
