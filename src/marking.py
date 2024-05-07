class Mark:
    __marked = []

    def __init__(self, pos: tuple[int, int]):
        self.id = len(self.__marked)
        self.__marked.append(self)

    def get_marked(self):
        return self.__marked

    @staticmethod
    def set_mark(pos: tuple[int, int]):
        raise NotImplementedError()

    def __del__(self):
        self.__marked.remove(self)
