class MedicineModel:
    def __init__(self, name:str, med_name:str, dosage:int):
        self.name = name
        self.medicine_name = med_name
        self.dosage = dosage

    def serialize(self) -> dict:
        return {
            "patient_name": self.name,
            "medicine_name": self.medicine_name,
            "dosage": self.dosage
        }
