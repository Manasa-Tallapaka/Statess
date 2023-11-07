from States.States import States
class Missouri(States):
    def __init__(self, special, location):
        super().__init__("Missouri","saint Louis" )
        self.location = location

    def get_info(self):
        return f"{super().get_info()} land for {self.location} Research."
