class student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.score = []

    def average(self):
        if len(self.score) == 0:
            return 0.0

        return sum(self.score) / len(self.score)

