class ExamModel:
    def __init__(self, name:str, issues:str, department:int):
        self.name = name
        self.issues = issues
        self.department = department

    def serialize(self) -> dict:
        return {
            "patient_name": self.name,
            "issues": self.issues,
            "department": self.department
        }