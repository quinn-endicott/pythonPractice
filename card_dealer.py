
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

#this function determines if a win has occurred and passes a string value to indicate
#how it happened, this is now in the card_dealer.py module
def turnResult(usrScore, dealerScore, hitVar):
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


def score(userHand, dealerHand):
    usrScore = 0
    dealerScore = 0
    uAceNum = 0
    dAceNum = 0
    aceList = []
    nAceList = []
    dAceList = []
    dNAceList = []
    aces = ['Ace of Spades', 'Ace of Hearts', 'Ace of Clubs', 'Ace of Diamonds']
    for usrKey, cardNum in userHand.items():
        usrScore += cardNum
        if usrKey in aces:
            uAceNum += 1
            aceList.append(cardNum)
        else:
            nAceList.append(cardNum)
    if uAceNum == 0:
        pass
    else:
        uHiAce = sum(aceList) + 10
        if (uHiAce + sum(nAceList)) <= 21:
            usrScore += 10

    for dlrKey, dCardNum in dealerHand.items():
        dealerScore += dCardNum
        if dlrKey in aces:
            dAceNum += 1
            dAceList.append(dCardNum)
        else:
            dNAceList.append(dCardNum)
    if dAceNum == 0:
        pass
    else:
        dHiAce = sum(dAceList) + 10
        if (dHiAce + sum(dNAceList)) <= 21:
            dealerScore += 10
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

