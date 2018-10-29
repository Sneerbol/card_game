from random import shuffle 

# useful variables for crating Cards.

Suite = 'H D S C'.split()
Ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()



class Deck:
    """
    This is the Dack Class. This Object will crate a deck of cards to initiate play.You can then use this Deck list of cards
    to split in half and give to the players. It will use SUITe and RANKS to create the deck. It should also have  a method
    for splitting/cutting the deck in half and Shuffing the deck.

    """
    def __init__(self):
        print("Creating New Ordered Deck!")
        self.allcards = [(s,r) for s Suite for r in Ranks ]

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcards)
    
    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])


class Hand:
    """
    This is the Hand Class. Each player has a Hand, and can add or remove cards from that hand. There should be an add and remove card method here.

    """
    def __init(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))
    
    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand class object.
    The Player can then play cards and check if they still have cards.

    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):

        drawn_card = self.hand.remove_card()

        
