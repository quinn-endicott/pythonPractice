
# This program uses a dictionary as a deck of cards.
import random

def uDeal(deck, times, userHand):
    for Ucard in range(times):
        UrandKey = random.choice(list(deck.keys()))
        UcardValue = deck.pop(UrandKey)
        userHand[UrandKey] = UcardValue
    return userHand
       
def dDeal(deck, times, dealerHand):
    for Dcard in range(times):
        DrandKey = random.choice(list(deck.keys()))
        DcardValue = deck.pop(DrandKey)
        dealerHand[DrandKey] = DcardValue
    return dealerHand

def printTurn(userHand, dealerHand, usrScore, dealerScore, turnNumber):
    print(f'Your cards, turn {turnNumber}: ')
    for uCard in userHand:
        print(uCard)
    print(f'Your Score is: {usrScore}\n')

    print(f"Dealer's cards, turn {turnNumber}: ")
    for dCard in dealerHand:
        print(dCard)
    print(f'Dealer score: {dealerScore}\n')

def deal(deck, times, hand):
    #for range(times passed as argument)
    for card in range(times):
        #select a random key from the deck
        randKey = random.choice(list(deck.keys()))
        #pop value from dictionary, card is now gone and cannot be drawn again
        cardValue = deck.pop(randKey)
        #add the chosen card to the user's hand
        hand[randKey] = cardValue
    #return userhand
    return hand

#this function determines if a win has occurred and passes a string value to indicate
#how it happened, this is now in the card_dealer.py module
def turnResult(usrScore, dealerScore, hitVar):
    if usrScore > 21 and dealerScore > 21:
        return True, 'both bust'
    #rare: if both user and dealer get 21 it's a tie, return true because game
    #is complete
    if usrScore == 21 and dealerScore == 21:
        return True, 'tie'
    #if user hits 21, user wins
    elif usrScore == 21:
        return True, 'user win'
    #if dealer hits 21, dealer wins
    elif dealerScore == 21:
        return True, 'dealer win'
    #if dealer wins because user busts out
    elif usrScore > 21:
        return True, 'user bust'
    #if user wins because dealer busts out
    elif dealerScore > 21:
        return True, 'dealer bust'
    #if user stands and dealer will not draw in next round
    elif dealerScore > 16 and hitVar != 'y':
        #if the user has more points than the dealer user wins
        if usrScore > dealerScore:
            return True, 'user win'
        #otherwise dealer wins
        else:
            return True, 'dealer win'
    #otherwise no one has won 
    else:
        return False, 'no win'



#winPrinter takes the winBool and win state variables and prints various statements
#based on who won and how they won, if there is no win, do nothing
def winPrinter(winBool, state):
    #if there is a winner
    if winBool is True:
        #if the user wins because higher score
        if state == 'user win':
            print('You Win!\n')
        elif state == 'both bust':
            print('Everyone looses!')
        elif state == 'tie':
            print("It's a tie!\n")
        # if the user won becuase dealer broke 21
        elif state == 'dealer bust':
            print('You Win! The dealer busted out.\n')
        # if dealer wins because you bust out
        elif state == 'user bust':
            print('The dealer won! You busted out.\n')
        # if dealer wins by points
        else:
            print('The dealer won!\n')
    # if winBool is false no one wins, do nothing
    else:
        pass


#score function scores the cards in each hand and returns the scores
def score(userHand, dealerHand):
    #initialize user score
    usrScore = 0
    #initialize dealerscore
    dealerScore = 0
    #counter for user aces
    uAceNum = 0
    #counter for dealer aces
    dAceNum = 0
    #empty list for user aces
    aceList = []
    #empty list for user non aces
    nAceList = []
    #dealer ace list
    dAceList = []
    #dealer non ace list
    dNAceList = []
    #list of keys for cards that are aces
    aces = ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']
    #for the card and card value in the user's hand
    for usrKey, cardNum in userHand.items():
        #base score is just the sum of card values
        usrScore += cardNum
        #if the user's card is an ace
        if usrKey in aces:
            #add 1 to aceNum
            uAceNum += 1
            #append the card value to aceList
            aceList.append(cardNum)
        #if card is not an ace
        else:
            #append value to non ace list
            nAceList.append(cardNum)
    #removed unnecessary if clause for no aces, if there are aces
    if uAceNum >= 1:
        #high value of the aces is sum(aceList)+10, 1 is valued as 11
        uHiAce = sum(aceList) + 10
        #if high ace value + sum(nAceList) is less than 21
        if (uHiAce + sum(nAceList)) <= 21:
            #add 10 to the usrScore
            usrScore += 10
    #logic for dealing with the dealer hand is the same
    for dlrKey, dCardNum in dealerHand.items():
        dealerScore += dCardNum
        if dlrKey in aces:
            dAceNum += 1
            dAceList.append(dCardNum)
        else:
            dNAceList.append(dCardNum)
    if dAceNum > 0:
        dHiAce = sum(dAceList) + 10
        if (dHiAce + sum(dNAceList)) <= 21:
            dealerScore += 10
    #return usrScore and dealerScore
    return usrScore, dealerScore







def create_deck():
# Create a dictionary with each card and its value
# stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    return deck

 # The deal_cards function deals a specified number of cards
 # from the deck.

def main():
# Create a deck of cards.
    deck = create_deck()
    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))

    # Deal the cards.
    deal_cards(deck, num_cards)

# The create_deck function returns a dictionary
# representing a deck of cards.

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value += deck[card]

    # Display the value of the hand.
    print(f'Value of this hand: {hand_value}')
# Call the main function.
if __name__ == '__main__':
    main()

