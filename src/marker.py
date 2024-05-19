class Marker:
    def __init__(self, start_pos: tuple[int, int], end_pos: tuple[int, int]):
        self.start_pos = start_pos
        self.end_pos = end_pos

    def get_area(self) -> tuple[tuple[int, int], tuple[int, int]]:
        return self.start_pos, self.end_pos
