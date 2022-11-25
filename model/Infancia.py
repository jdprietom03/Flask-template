class Infancia:
    def __init__(self, body, **kwargs):
        self.__dict__.update(kwargs)
        self.__dict__.update(body)