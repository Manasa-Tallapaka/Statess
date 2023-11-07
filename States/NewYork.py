from States.States import States
class NewYork(States):
    def __init__(self, special, location):
        super().__init__("NewYork", special)
        self.location = location

    def get_info(self):
        return f"{super().get_info()} is the busiest {self.location} location."
