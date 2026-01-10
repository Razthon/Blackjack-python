#==========================
#Imports
#==========================

import random



#==========================
#Modules
#==========================

hitlist = []
def main():
    chipcount = 100
    gameloop = "Y"
    
    wincount = 0
    losscount = 0
    while gameloop.upper() == "Y":
        if chipcount == 0:
            print("The house always wins! You have no more chips left. \nThanks for playing!\n**Try FreeChips next time to get some extra chips!**")
            gameloop = "N"
        betting = True
        while betting == True:
            bet = input(f"You have {chipcount} chips. How many would you like to bet? ")
            if bet == "FreeChips":
                chipcount += 100
                print("You have been awarded 100 free chips!")
            elif not bet.isdigit():
                print("Please enter a valid number.")
            elif int(bet) > chipcount or int(bet) <= 0:
                print("You cannot bet more chips than you have or less than 1.")
            else:
                betting = False
        bet = int(bet)
        dealnum1 = get_numbers()
        dealnum2 = get_numbers()
        playernum1 = get_numbers()
        playernum2 = get_numbers()
        wincount, losscount, chipcount = game(dealnum1, dealnum2, playernum1, playernum2, wincount, losscount, bet, chipcount)
        print(f"Win count: {wincount}, Loss count: {losscount}")
        validgameloop = False
        while validgameloop == False:
            gameloop = input("Do you want to play again? Y/N: ")
            if gameloop == "FreeChips":
                chipcount += 100
                print("You have been awarded 100 free chips!")
            elif gameloop.upper() == "Y":
                validgameloop = True
            elif gameloop.upper() == "N":
                print("Thanks for playing!")
                validgameloop = True
            else:
                print("Please enter 'Y' or 'N'.")


def get_numbers():
    num = random.randint(1, 13) # Generate a random number between 1 and 13
    if num == 1:
        return 'A'
    elif num == 11:
        return 'J' 
    elif num == 12:
        return 'Q'
    elif num == 13:
        return 'K'
    else:
        return num



#==========================
#Main Game Logic
#==========================



def game(dealnum1, dealnum2, playernum1, playernum2, wincount, losscount, bet, chipcount):
    hitlist.clear()
    hit = True
    hits = 0
    print(f"Dealer showing: {dealnum1}")
    print(f"Player's cards: {playernum1}, {playernum2}")
    while hit == True:
        choice = input("Would you like to hit or stand? h/s: ")
        if choice == 'h':
            print("You chose to hit.")
        elif choice == 's':
            print("You chose to stand.")
            hit = False
        else:
            print("Invalid input. Please enter 'h' or 's'.")
        if choice == 'h':
            newcard = get_numbers()
            hitlist.append((newcard))
            hits += 1
            print(f"You drew a {newcard}.")
    print("Final hand:")
    print(playernum1)
    print(playernum2)
    for item in hitlist:
        print(item)
    total, blackjack = calculate_playertotal(playernum1, playernum2, hitlist)
    if total > 21:
        print("Bust! You lose.")
        losscount += 1
        chipcount -= bet
        print(f"You lost your bet, total chipcount is now {chipcount}.")
    elif blackjack == True:
        print("Blackjack! You win 1.25 times your bet.")
        wincount += 1
        chipcount += int(bet * 1.25)
        print(f"You won your bet, total chipcount is now {chipcount}.")
        blackjack = False
    else:
        print(f"Dealer's first card is {dealnum1}")
        print(f"Dealer's second card is {dealnum2}")
        dealertotal = calculate_dealertotal(dealnum1, dealnum2)
        if dealertotal > 21:
            print("Dealer busts! You win.")
            wincount += 1
            chipcount += bet
            print(f"You won your bet, total chipcount is now {chipcount}.")
        elif dealertotal < total:
            print("You win!")
            wincount += 1
            chipcount += bet
            print(f"You won your bet, total chipcount is now {chipcount}.")
        elif dealertotal > total:
            print("Dealer wins!")
            losscount += 1
            chipcount -= bet
            print(f"You lost your bet, total chipcount is now {chipcount}.")
        else:
            print("Push! It's a tie.")
    return wincount, losscount, chipcount



#==========================
#Player Total and Dealer Total Calculation
#==========================

def calculate_playertotal(playernum1, playernum2, hitlist):
    total = 0
    blackjack = False
    card_values = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}
    
    def card_value(card):
        if isinstance(card, int):
            return card
        return card_values.get(card, 0)
    
    total += card_value(playernum1)
    total += card_value(playernum2)
    if total == 21 and len(hitlist) == 0:
        print("Blackjack!")
        blackjack = True
    

    for item in hitlist:
        total += card_value(item)
    if "A" in [playernum1, playernum2] + hitlist and total > 21:
        total -= 10
    print(f"Your total is: {total}")
    return total, blackjack


def calculate_dealertotal(dealnum1, dealnum2):
    total = 0
    card_values = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}
    
    def card_value(card):
        if isinstance(card, int):
            return card
        return card_values.get(card, 0)
    
    total += card_value(dealnum1)
    total += card_value(dealnum2)
    
    if "A" in [dealnum1, dealnum2] and total > 21:
        total -= 10

    if total < 17:
        while total < 17:
            newcard = get_numbers()
            print(f"Dealer draws a {newcard}.")
            total += card_value(newcard)
            if newcard == "A" and total > 21:
                total -= 10
    
    print(f"Dealer's total is: {total}")
    return total









main()