from random import randint
from IPython.display import clear_output
class Blackjack():
    def __init__(self):
        self.deck =[]
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2,3,4,5,6,7,8,9,10,'J','Q', 'K','A')
    def makeDeck(self):
        for suits in self.suits:
            for value in self.values:
                self.deck.append((value, suits)) 
    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) -1))
class Player():
    def __init__(self, name):
        self.name = name
        self.hand =[ ]
    #take in a tuple and append it to the hand
    def addCard(self, card):
        self.hand.append(card)
    def showHand(self, dealer_start = True):
        print('\n{}'.format(self.name))
        print('===========')
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i ==0 and dealer_start:
                print('- of -') # hide first card
            else:
                card = self.hand[i]
                print('{} of {}'.format(card[0], card[1]))
        print('Total = {}'.format(self.calcHand(dealer_start)))
        #if not dealer's turn then only give back total of second card
    def calcHand(self, dealer_start =True):
        total=0
        aces = 0

        card_values ={1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}
        if self.name =='Dealer' and dealer_start:

            card = self.hand[1]
            return card_values [card[0]]
        for card in self.hand:
            if card[0] == 'A':
                aces += 1
            else:
                total += card_values[card[0]]
        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total
game = Blackjack()
game.makeDeck()

name = input('What is your name?')
player = Player(name)
dealer = Player('Dealer')


#add two cards to the dealer and player hands

for i in range(2):
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())
#show using both hands
player.showHand()
dealer.showHand()
#handling the players turn

bust_player = False #keeps player going over 21
while input('Would you like to stay or hit?').lower() != 'stay':
    clear_output()
    #pull card and put into players hand
    player.addCard(game.pullCard())
    #show both hands using method
    player.showHand()
    dealer.showHand()
    #check if over 21
    if player.calcHand() > 21:
        bust_player = True
        #print('You lose')
        break
#handling dealers turn, if player didn't bust
dealer_bust = False
if not bust_player:
    while dealer.calcHand(False) < 17:
        #pull card and put into players hand
        dealer.addCard(game.pullCard())
        #check if over 21
        if dealer.calcHand(False) > 21:
            dealer_bust = True
           # print('You win')
            break
clear_output()
#show both hands using method
player.showHand()
dealer.showHand(False)
#pass false to calculate and show all cards even when there are two

#calculating the winner
if bust_player:
    print ('You are busted!! Better luck next time')
elif dealer_bust:
   print('The dealer is busted you win')
elif dealer.calcHand(False) > player.calcHand():
    print('Dealer has higher cards, you Lose!!')
elif dealer.calcHand(False) < player.calcHand() :
   print('You beat the dealer!! You Won')
else:
    print('You pushed, no one wins')



#print("Player Hand:{}\n Dealer Hand: {}".format(player.hand, dealer.hand))

#print(player.name, dealer.name)
#print(game.pullCard( ), len(game.deck))
#print(game.deck)
