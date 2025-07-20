import random

class TipsGenerator:
    def get_tip(self):
        tips = [
            "Use strong, unique passwords for each account.",
            "Enable two-factor authentication.",
            "Think before you click suspicious links.",
            "Keep your software updated.",
            "Don't share personal info publicly online."
        ]
        return random.choice(tips)
