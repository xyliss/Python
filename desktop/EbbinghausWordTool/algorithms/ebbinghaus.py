from datetime import datetime, timedelta


class Ebbinghaus_hy:
    def __init__(self):
        self.review_days = [1, 2, 4, 7, 15, 30]

    def update_review_hy(self, word, status):
        """
        status:
        know = 认识
        vague = 模糊
        forget = 不会
        """

        if status == "know":
            if word.stage < len(self.review_days) - 1:
                word.stage += 1

        elif status == "vague":
            pass

        elif status == "forget":
            word.stage = 0

        interval = self.review_days[word.stage]

        word.next_review = (
            datetime.now() + timedelta(days=interval)
        ).strftime("%Y-%m-%d")

        word.review_count += 1

        if word.stage >= 5:
            word.mastered = True

        return word