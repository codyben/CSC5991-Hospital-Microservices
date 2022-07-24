from distutils.command.clean import clean
from os import times


class CleaningStaffModel:
    def __init__(self, name:str, days_available:str, times_available:str, cleaning_area:str):
        self.name = name
        self.days_available = days_available
        self.times_available = times_available
        self.cleaning_area = cleaning_area


    def serialize(self) -> dict:
        return {
            "name": self.name,
            "days_available": self.days_available,
            "times_available": self.times_available,
            "cleaning_area": self.cleaning_area
        }