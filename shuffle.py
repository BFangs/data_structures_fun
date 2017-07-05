from stacks import Stack

class Deck(object):
    """deck of cards"""
    def __init__(self):
        self.deck = 4 * range(13)

    def __repr__(self):
        return "My deck of cards!"

    def len(self):
        return len(self.deck)

    def view(self):
        return self.deck

    def shuffle(self, cut=26):
        left = Stack(self.deck[:cut:-1])
        right = Stack(self.deck[cut::-1])
        shuffled = []
        while left.stack and right.stack:
            shuffled.append(right.pop())
            shuffled.append(left.pop())
        shuffled.extend(left)
        shuffled.extend(right)
        self.deck = shuffled
        return self.deck
