from vvsa.conf import global_settings
from vvsa.conf import matplotlib


class Settings:
    def __init__(self):
        for setting in dir(global_settings):
            setattr(self, setting, getattr(global_settings, setting))


settings = Settings()
