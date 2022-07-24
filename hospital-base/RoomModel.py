class RoomModel:
    def __init__(self, name:str, number:int, department:str):
        self.name = name
        self.number =  number
        self.department = department

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "room_number": self.number,
            "department": self.department
        }