class AmbulanceModel:
    def __init__(self, name:str, number:int, days_available:str, times_available:str):
        self.name = name
        self.ambulance_number = number
        self.days_available = days_available
        self.times_available = times_available


    def serialize(self) -> dict:
        return {
            "name": self.name,
            "ambulance_number": self.ambulance_number,
            "days_available": self.days_available,
            "times_available": self.times_available
        }