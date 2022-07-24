class PatientModel:
    def __init__(self, name:str, age:int, phone:str, patient_id:int):
        self.name = name
        self.age = age
        self.phone = phone
        self.id = patient_id

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "patient_id": self.id
        }