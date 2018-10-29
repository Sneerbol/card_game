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
        self.allcards = [(s,r) for s in Suite for r in Ranks]

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcards)
    
    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])


class Hand:
    """
    This is the Hand Class. Each player has a Hand, and can add or remove cards from that hand. There should be an add and remove card method here.

    """
    def __init__(self, cards):
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
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
        
        return war_cards

    def still_has_cards(self):

        return len(self.hand.cards) != 0


    # GAME PLAY #

print("Welcome to War, let's begin...")


#create new deck and split it in half

d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#create both players
computer = "computer"
comp = Player(computer, Hand(half1))
name = "Gamer"
user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("here are the current stanings")
    print(user.name+"has the count: "+str(len(user.hand.cards)))
    print(comp.name+"has the count: "+str(len(comp.hand.cards)))
    print("play a card!")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if Ranks.index(c_card[1]) < Ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards) 
    else:
        if Ranks.index(c_card[1]) < Ranks.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            comp.hand.add(table_cards)


print("Game over, number of round:"+str(total_rounds))
print("a war happened "+str(war_count)+"times")
if str(comp.still_has_cards()) == "True" and str(user.still_has_cards()) == "False":
    print("Computer won")
else:
    print("User won")



        




















    




















    


    


        
