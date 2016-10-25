"""

This module contains code from
Think Python: an Introduction to Software Design
Allen B. Downey

Modified by Paul Resnick for SI/EECS 182,
Sean Munson for HCDE 310

"""

import random

class Card(object):
    """represents a standard playing card."""
    # class variables shared by all instances
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
            "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                         Card.suit_names[self.suit])

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

Card()
Card(3, 7)

class SetOfCards(object):
    " represents a set of cards"
    def __init__(self):
        self.cards = []

    def __str__(self):
        res_string =""
        for x in self.cards:
            res_string += str(x)  + '\n'
            #x.__str__()   or just say str(x)
#            res_string = res_string + str(x) + '\n'  
        return res_string 

    def add_card(self, card):
        """add a card to the deck"""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """remove and return a card from the deck.
    By default, pop the last card."""
        return self.cards.pop(i)

    def shuffle(self):
        """shuffle the cards in this set: this is magic for now"""
        random.shuffle(self.cards)

    def sort(self):
        """sort the cards in ascending order"""
        self.cards.sort()

    def move_cards(self, hand, num):
        """move the given number of cards from the self collection into the hand collection"""
        for i in range(num):
            hand.add_card(self.pop_card())

class Deck(SetOfCards):
    """represents a deck of cards"""
  
    def __init__(self):
        self.cards=[]
        self.make_cards()
        self.shuffle()

    def make_cards(self):
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)



def find_defining_class(obj, meth_name):
    """find and return the class object that will provide 
      the definition of meth_name (as a string) if it is
      invoked on obj."""
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()

    hand = SetOfCards()
    print find_defining_class(hand, 'shuffle')
    print find_defining_class(deck, 'shuffle')
    
    print hand.cards
    print len(deck.cards)
    deck.move_cards(hand, 5)
    print "----after cards moved"
    print len(deck.cards)
    print hand.cards
    print hand
    hand.shuffle()
    print "----after hand is shuffled"
    print hand
    hand.shuffle()
    print "----after second shuffle"
    print hand
    

