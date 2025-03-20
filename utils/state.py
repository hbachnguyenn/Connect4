import score


class State:
    board: [[bool | None]]
    evaluation_value: int

    def __init__(self, board: [[bool | None]]):
        self.board = board
        self.evaluation_value = 0

    def get_evaluation_value(self):
        return self.evaluation_value

    def calculate_evaluation_value(self):
        pass

    def generate_next_state(self):
        pass