from datetime import datetime


class Word_hy:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.stage = 0
        self.review_count = 0
        self.mastered = False
        self.next_review = datetime.now().strftime("%Y-%m-%d")
        self.create_date = datetime.now().strftime("%Y-%m-%d")

    def to_dict_hy(self):
        return {
            "word": self.word,
            "meaning": self.meaning,
            "stage": self.stage,
            "review_count": self.review_count,
            "mastered": self.mastered,
            "next_review": self.next_review,
            "create_date": self.create_date
        }

    @classmethod
    def from_dict_hy(cls, data):
        word = cls(data["word"], data["meaning"])
        word.stage = data["stage"]
        word.review_count = data["review_count"]
        word.mastered = data["mastered"]
        word.next_review = data["next_review"]
        word.create_date = data["create_date"]
        return word