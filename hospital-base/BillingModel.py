from os import times


class BillingModel:
    def __init__(self, name:str, owed:int, due_by:str):
        self.name = name
        self.owed = owed
        self.due_by = due_by


    def serialize(self) -> dict:
        return {
            "name": self.name,
            "due_by": self.due_by,
            "owed": self.owed
        }