class DiagnosticsModel:
    def __init__(self, name:str, number:int, procedure:str):
        self.name = name
        self.ambulance_number = number
        self.procedure = procedure
       


    def serialize(self) -> dict:
        return {
            "name": self.name,
            "ambulance_number": self.ambulance_number,
            "procedure": self.procedure
        }