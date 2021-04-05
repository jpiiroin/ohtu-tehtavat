
class Summa:
    def __init__(self, io, luku):
        self.io = io
        self.luku = luku

    def suorita(self):
        self.io.plus(self.luku)
