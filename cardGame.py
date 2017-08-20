from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#List of all the cards in the deck
mycards = [(s,r) for s in SUITE for r in RANKS]

class Deck:
    """
    This is the Deck Class.
    Creates a deck of cards.
    Shuffle method
    Split method
    """
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = mycards

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    '''
    This is the Hand class.
    Add/Remove methods
    '''
    def __init__(self,cards):
        self.cards = cards

    def  __str__(self):
        return "Contains {} cards".formate(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    Player Class
    """

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        draw_card = self.hand.remove_card()
        print("{} has placed:{}".format(self.name,draw_card))
        print("\n")
        return draw_card

    def remove_war_card(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        Checks to see if the player still has cards
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#Create a new deck and split it to half:
d = Deck()
d.shuffle()

#tuple un-packing
half1,half2 = d.split_in_half()

#Create Players!
system = Player("System",Hand(half1))

name = input("what is our name?")
user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and system.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Current Standings")
    print(user.name+"has the count:"+str(len(system.hand.cards)))
    print("play a card!")
    print('\n')

    table_cards=[]

    s_card = system.play_card()
    p_card = user.play_card()

    table_cards.append(s_card)
    table_cards.append(p_card)

    if s_card[1] == p_card[1]: #Checking the system card RANK vs the user card RANK
        war_count += 1
        print("We have a War!")

        table_cards.extend(user.remove_war_card())#3 cards from the user eck
        table_cards.extend(system.remove_war_card())

        if RANKS.index(s_card[1]) < RANKS.index(p_card[1]):#system card is less than the player card
            user.hand.add(table_cards)
        else:
            system.hand.add(table_cards)
    else:
        if RANKS.index(s_card[1]) < RANKS.index(p_card[1]):#system card is less than the player card
            user.hand.add(table_cards)
        else:
            system.hand.add(table_cards)

print("Game over, number of rounds played {}".format(total_rounds))
print("A war happened {} times".format(war_count))
print("System has cards? {system_count} and {user} has cards? {user_count}".format(system_count=system.still_has_cards(),user=name,user_count=user.still_has_cards()))
