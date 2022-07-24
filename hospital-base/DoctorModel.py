class DoctorModel:
    def __init__(self, name:str, phone:str, field:str, present:str, times:str):
        self.name = name
        self.field = field
        self.phone = phone
        self.present = present
        self.times = times

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "present": self.present,
            "phone": self.phone,
            "times": self.times
        }