class Row:
    def __init__(self, contents: str):
        char_map = {"r": True, "y": False}
        self.list_rows = [[char_map.get(char, None) for char in item] for item in contents.split(",")]

        self.score_red = 0
        self.score_yellow = 0

    #
    # def calculate_score(self, color: str):
    #     color = "r" if color == "red" else "y"
    #     for row in self.list_rows:
    #
    #         for i in row:

    def get_list(self):
        return self.list_rows