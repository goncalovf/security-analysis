from abc import ABC


class Economic_Indicator(ABC):
    def __init__(self, name):
        self.name = name
