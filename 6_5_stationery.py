class Stationery:
    title = 'title'

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        super().draw()
        print(f"But now your draw with {self.title}. We couldn't wash it out")


class Pensil(Stationery):
    title = 'Pensil'

    def draw(self):
        super().draw()
        print(f"{self.title} is your rational choice")


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        super().draw()
        print(f"{self.title} is for brave people only")


pen = Pen()
pen.draw()
pensil = Pensil()
pensil.draw()
handle = Handle()
handle.draw()
