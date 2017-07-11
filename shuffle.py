from stacks import Stack
from random import choice

class CardError(Exception):
    def __init__(self, msg):
        super(CardError, self).__init__(msg + (": unable to execute!"))

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

    def shuffle(self, cut=26, skill=1):
        left = Stack(self.deck[:cut:-1])
        right = Stack(self.deck[cut::-1])
        shuffled = []
        if not isinstance(skill, int) or skill < 0 or skill > 1:
            raise CardError("Invalid input: check the skill parameters!")
        if not isinstance(cut, int) or cut < 0 or cut > 52:
            raise CardError("Invalid input: check the cut parameters!")
        if skill == 1:
            constant = True
        if skill != 1:
            percentage_error = 1 - skill
            possible_error = int(min(left, right) * percentage_error)
            possibilities = range(1, possible_error + 2)
        while left.stack and right.stack:
            if not constant:
                try:
                    shuffled.append(right.pop(choice(possibilities)))
                except:
                    shuffled.extend(right)
                try:
                    shuffled.append(left.pop(choice(possibilities)))
                except:
                    shuffled.extend(left)
            else:
                shuffled.append(right.pop())
                shuffled.append(left.pop())
        shuffled.extend(left)
        shuffled.extend(right)
        self.deck = shuffled
        return self.deck
