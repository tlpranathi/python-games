import random


suits = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

game = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_1(self):
        return self.cards.pop()
    
# d1 = Deck()
# d1.shuffle()
# for i in range(52):
#     print(d1.cards[i])
# print("************")
# print(d1.deal_1())
# d1 = Deck()
# print(d1)


class Hand:
    def __init__(self):
        self.my_cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.my_cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# d1 = Deck()
# d1.shuffle()
# p1 = Hand()
# p1.add_card(d1.deal_1())
# p1.add_card(d1.deal_1())
# print(p1.value)
# for card in p1.my_cards:
#     print(card)


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win(self):
        self.total += self.bet
    
    def lose(self):
        self.total -= self.bet


def take_bets(chips):
    while True:
        try: 
            chips.bet = int(input("\nHow many chips do you want to bet?: "))
        
        except ValueError:
            print("\nEnter a valid number!!")
        
        else:
            if chips.bet > chips.total:
                print("\nYour bet can't exceed ", chips.total)

            elif chips.bet <= 0:
                print("\nYour bet can't be zero or negative!!!")

            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal_1())
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global game

    while True:
        mv = input("Do you want to hit or stand? (h or s): ").strip()
        
        if mv[0].lower() == "h":
            hit(deck, hand)
        
        elif mv[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            game = False
        
        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\n***Dealer's Hand***")
    print("<card hidden>")
    print(dealer.my_cards[1]) 
    print("\n***Player's Hand***", *player.my_cards, sep='\n')
    

def show_all(player, dealer):
    print("\n***Dealer's Hand:***", *dealer.my_cards, sep='\n')
    print("Dealer's Hand =",dealer.value)
    print("\n***Player's Hand:***", *player.my_cards, sep='\n')
    print("Player's Hand =",player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


player_chips = Chips() 

print("Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until they reach 17. Aces count as 1 or 11.")

while True:
    print(f"Current chip count: {player_chips.total}. Place your bet!")
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_1())
    player_hand.add_card(deck.deal_1())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_1())
    dealer_hand.add_card(deck.deal_1()) 
    
    take_bets(player_chips)
    
    show_some(player_hand, dealer_hand)
    
    while game:
        hit_or_stand(deck, player_hand) 
        
        show_some(player_hand, dealer_hand)  
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break        


    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)        
    
    print("\nPlayer's winnings stand at:", player_chips.total)

    if player_chips.total > 0:
        new_game = input("Would you like to play another hand? Enter(y / n): ").strip()
        if new_game[0].lower() == "y":
            game = True
            print("You know the rules!")
            continue
    
        else:
            print("Good game! May your chips stack higher next time.")
            break
    
    elif player_chips.total == 0:
        reset_game = input("No chips left on the table! Would you like to reload 100 chips and stay in the game? Enter(y / n): ").strip()
        if reset_game[0].lower() == "y":
            player_chips.total = 100
            game = True
            print("Chips reloaded!")
            continue
    
        else:
            print("Good game! May your chips stack higher next time.")
            break
    



# HANDLE LOSING ALL CHIPS >>> done
# USE TIME MODULE >>> nah just looks like its buffering
# DISPLAY CHIPS IN THE BEGINNING OF THE GAME >>> done
# DONT PRINT WELCOME LINE WHEN PLAYING SECOND TIME!! >>> done
# DONT TAKE NEGATIVE BETS >>> done