from abc import ABC, abstractmethod
class States:
    def __init__(self, name, special):
        self.name = name
        self.special = special

    def get_info(self):
        return f"{self.name} {self.special}."



