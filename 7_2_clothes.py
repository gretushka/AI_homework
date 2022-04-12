from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_cons(self):
        pass


class Suit(Clothes):
    height = 0

    def __init__(self, h):
        try:
            if int(h) == h:
                self.height = h
        except ValueError:
            pass

    @property
    def fabric_cons(self):
        return 2 * self.height + 0.3


class Coat(Clothes):
    volume = 0

    def __init__(self, v):
        try:
            if int(v) == v:
                self.volume = v
        except ValueError:
            pass

    @property
    def fabric_cons(self):
        return self.volume / 6.5 + 0.5


suits = [Suit(i) for i in range(1, 6)]
for i, suit in enumerate(suits):
    print(f"For suit of size {i + 1} we need {suit.fabric_cons} meters of fabric")
print(
    f'For 5 suits of size 3 and 3 coats of volume 50 we need {5 * Suit(3).fabric_cons + 3 * Coat(50).fabric_cons:.2f} meters of fabric')
