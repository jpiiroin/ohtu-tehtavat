class Summa:
    def __init__(self, io, luku):
        self.io = io
        
        self.luku = luku

    def suorita(self):
        if isinstance(self.luku, int):
            self.io.plus(self.luku)
        else:
            print("ei int!")
            print(self.luku)