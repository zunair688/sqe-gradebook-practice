class student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.score = []

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score.append(score)

    def average(self):
        if len(self.score) == 0:
            return 0.0

        return sum(self.score) / len(self.score)

