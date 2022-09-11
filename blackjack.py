import random

suits  = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = {'Ace':1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
 'Seven': 7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen': 10, 'King':10}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = ranks[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Player():
    def __init__(self, balance:float):
        self.balance = balance
        self.hand = []
    
    def hand_total(self):
        total = 0
        if len(self.hand) > 0:        
            for card in self.hand:
                total += card.value
        return total
    
    def add_card(self, new_card):
        self.hand.append(new_card)
    
    def clear_cards(self):
        self.hand.clear()
    
    def bet(self, amount: float):
        self.balance -= amount
    
    def add_winnings(self, amount):
        self.balance += amount
        

    def __str__(self):
        return f'The player has a balance of {self.balance}'


class Dealer():
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks.keys():
                self.deck.append(Card(suit, rank))
        
        random.shuffle(self.deck)
        self.hand = []
    
    def get_fresh_deck(self):
        self.deck.clear()
        for suit in suits:
            for rank in ranks.keys():
                self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)

    def hand_total(self):
        total = 0
        if len(self.hand) > 0:        
            for card in self.hand:
                total += card.value
        return total

    def add_card(self, new_card):
        self.hand.append(new_card)


    def deal(self):
        return self.deck.pop(-1)
    
    def show_one_card(self):
        if len(self.hand) > 0:
            return self.hand[-1]


print('Welcome to BLACKJACK')
player_bank = input('How much are you starting with: ')

while not player_bank.isdigit():
    player_bank = input('Please enter a valid amount: ')


player = Player(float(player_bank))
dealer = Dealer()


while True:
    amount_in_bank = player.balance
    bet_amount = input('Enter a bet amount: ')

    while not bet_amount.isdigit():
        bet_amount = input('Enter a bet amount (Integer or float): ')

    while float(bet_amount) > amount_in_bank:
        bet_amount = input(f'Insufficient balance. Please enter an amount not greater than {amount_in_bank}: ')
        while not bet_amount.isdigit():
            bet_amount = input('Enter a bet amount (Integer or float): ')

    player.bet(float(bet_amount))
    pot = float(bet_amount)

    round_on = True
    player_wins = False
    house_wins = False

    
    for i in range(0,2):
        player.add_card(dealer.deal())
        dealer.add_card(dealer.deal())
    

    dealer_card = dealer.show_one_card()
    print(f"Player, the dealer's card is {dealer_card}")
   

    while True:
        print(f'Player this is your current total: {player.hand_total()}')
        player_action = input('hit (h) or stay (s)')
        if player_action == 's':
            break
        if player_action == 'h':
            player.add_card(dealer.deal())
            if player.hand_total() == 21:
                player_wins = True
                break
            if player.hand_total() > 21:
                print('Bust!!!')
                house_wins = True
                break
    
    if player_action == 's':
        while True:
            dealer.add_card(dealer.deal())
            if dealer.hand_total() > 21:
                player_wins = True
                break
            else:
                if dealer.hand_total()  > player.hand_total():
                    print(f'The dealer total is {dealer.hand_total()} while player total is {player.hand_total()}')
                    house_wins = True
                    break

    if player_wins:
        print('You won this round')
        player.add_winnings(2*pot)
    if house_wins:
        print('The house wins!')

    quit_game = input('Quit? y or n: ')
    if quit_game == 'y':
        print(f'Your final balance is {player.balance}')
        break
    dealer.get_fresh_deck()
    player.clear_cards()
    


