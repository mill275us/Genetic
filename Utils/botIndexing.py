class BotTracker:
    def __init__(self) -> None:
        self.next_id = 0

    def getId(self):
        self.next_id += 1
        return self.next_id