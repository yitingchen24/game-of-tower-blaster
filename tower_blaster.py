
import random

def setup_bricks():
    """ Creates a main pile of 60 bricks, represented as a list containing the integers 1 – 60.
    Creates a discard pile of 0 bricks, represented as an empty list.
    """
    print("Setting up the bricks to start the game")
    main_pile = [x for x in range(1,61)]
    discard_pile = []
    return main_pile, discard_pile

def shuffle_bricks(bricks):
    """Shuffle the given bricks (represented as a list), does not return anything."""

    print("Shuffling bricks.....")
    random.shuffle(bricks)

def check_bricks(main_pile, discard_pile):
    """ Check if there are any cards left in the given main pile of bricks. 
     If not, shuffle the discard pile (using the shuffle function) and move those bricks to the main pile."""

    if(len(main_pile) == 0):
        print("No bricks left in the main pile")

        shuffle_bricks(discard_pile)
        
        print("Copy discard_pile to main_pile")
        main_pile[:] = discard_pile[:]
        discard_pile[:] = []
        add_brick_to_discard(main_pile.pop(0), discard_pile) 

def check_tower_blaster(tower):
    """ Given a tower (the user’s or the computer’s list), determine the bricks are in ascending order."""
    
    #Created a new sorted list using python sorted function, check if this tower's value is the same as the new sorted list. 
    sortedTower = sorted(tower)
    if(tower == sortedTower):
        return True
    return False

def get_top_brick(brick_pile):
    """ Remove and return the top brick from any given pile of bricks."""

    #Check first to see if brick_pile is empty so that we won't have a compile error
    if(len(brick_pile) == 0):
        return None
        
    return brick_pile.pop(0)

def deal_initial_bricks(main_pile):
    """ Start the game by dealing two sets of 10 bricks each, from the given main_pile. 
    This function returns a tuple containing two lists, the first one representing the computer’s hand and the second one representing the user’s hand.
    """
    computer_hand = []
    human_hand = []
    
    #Deal 10 cards each to computer and human
    for i in range(10):
        computer_hand.insert(0, main_pile.pop(0))
        human_hand.insert(0, main_pile.pop(0))
    return computer_hand, human_hand

def add_brick_to_discard(brick, discard):
    """ Add the given brick (represented as an integer) to the top of the given discard pile (which is a list)"""
    discard.insert(0, brick)

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """Find the given brick to be replaced (represented by an integer) in the given tower and replace it with the given new brick."""

    #check to see if the brick to be replaced is actually in the list
    if brick_to_be_replaced in tower:
        #get index of that brick in the list
        index = tower.index(brick_to_be_replaced)
        #change to the new brick
        tower[index] = new_brick

        #add the discarded brick to the discard list
        add_brick_to_discard(brick_to_be_replaced, discard)
        return True
    else:
        return False

def computer_play(tower, main_pile, discard):
    #the first choice for computer is the top card from discard
    card = discard[0]
    
    #get card index
    card_index = int((card - 1) / 6)   

    #if previous card in tower is greater than this card, then replace it
    if(tower[card_index] > card):
        find_and_replace(get_top_brick(discard), tower[card_index], tower, discard)
        print("Computer gets card", card, "from discard pile")

    #else choose card from main pile
    else:
        card = get_top_brick(main_pile)
        card_index = int((card - 1) / 6)

        find_and_replace(card, tower[card_index], tower, discard)
        print("computer gets card", card, "from main pile")

    return tower

def user_turn(tower, discard):
    """Starts the user's turn"""

    print("Now it's your turn...")
    print("Your tower is:")
    print(tower)

    top_discard_card = discard[0]
    print("The top brick in discard pile is ", top_discard_card)

def human_play(tower, main_pile, discard):
    
    #starts the user's turn
    user_turn(tower,discard)

    print("")
    print("")
     
    #initalize a new brick to be none
    newBrick = None
    use_new_brick = False
    while(use_new_brick == False):
        try: 
            #ask user to choose from discard pile or main pile
            choice = input("Type D for the discard brick, M for the mystery brick... ")
            
            #if user choose to use card from discard pile, user has to use it
            if(choice.lower() == 'd'):
                newBrick = get_top_brick(discard)
                print("You chose", newBrick, "from discard pile")

                while(True):
                    try:

                        #ask user which brick he wants to replace, keep checking until user choose a valid number
                        brick_to_be_replaced = int(input("Which brick do you want to change? You have to choose one brick from your tower"))  
                         
                        #is answer is valid, break the while loop
                        if(brick_to_be_replaced in tower):
                            break
                       
                        #if answer is not valid, ask user to choose again
                        else:
                            print("The brick you choose is not in your tower")
                            continue
                    
                    except:
                        print("invalid input")
                        continue
                
                #place this brick in user's tower
                use_new_brick = find_and_replace(newBrick, brick_to_be_replaced, tower, discard)
           
            #if user chooses card from main pile instead, he can choose if he wants to use the card
            elif(choice.lower() == 'm'):
                newBrick = get_top_brick(main_pile)
                print("You chose", newBrick, "from main pile")

                while(True):

                    try: 
                        #ask the user if he wants to use it                 
                        ans = input("Do you want to use this brick from main pile? Y / N")

                        #if yes
                        if(ans.lower() == 'y'):

                            while(True):
                                try:
                                    #ask which brick user wants to replace
                                    brick_to_be_replaced = int(input("Which brick do you want to change? You have to choose one brick from your tower"))  
                                    if(brick_to_be_replaced in tower):
                                        break
                                    else:
                                        print("The brick you choose is not in your tower")
                                        continue
                                
                                except:
                                    print("invalid input")
                                    continue

                            use_new_brick = find_and_replace(newBrick, brick_to_be_replaced, tower, discard)
                            break

                        #is user doesn't want to use the card, then return the original tower
                        elif(ans.lower() == 'n'):
                            add_brick_to_discard(newBrick, discard)
                            print("You chose to discard this card from main pile")
                            return tower
                        
                        else:
                            print("Invalid input")
                            continue
                    
                    #keeps asking user until gets valid input
                    except:
                        print("invalid input") 
                        continue
            else:
                print("invalid input")          
                continue
        #keeps asking user until gets valid input
        except:
            print("invalid input") 
            continue
        
    
    return tower

def main():
    
    #set up bricks
    main_pile, discard_pile = setup_bricks()
    
    #shuffle bricks
    shuffle_bricks(main_pile)
    
    #deal initial bricks 
    computer_hand, user_hand = deal_initial_bricks(main_pile)
    
    #add one card to discard so discard pile is not empty
    add_brick_to_discard(get_top_brick(main_pile), discard_pile)
    
    #print initial tower for both
    print("Computer goes first...")
    print("Computer Hand is :", computer_hand)
    print("")
    print("Your hand is: ", user_hand)

    print("")
    print("")
   
    #check to see if either computer or user wins at the initial deal
    if(check_tower_blaster(computer_hand)):
        print("Computer won, game Over!")
        return
    
    if(check_tower_blaster(user_hand)):
        print("You already won")
        return

    while(True):
        
        #check if main_pile is empty
        check_bricks(main_pile, discard_pile)
        
        print("Computer 's turn to choose")
        #computer's turn
        computer_hand = computer_play(computer_hand, main_pile, discard_pile)
        print(computer_hand)

        print("")
        print("")
        
        #check if computer won
        if(check_tower_blaster(computer_hand)):
            print("Computer won, game Over!")
            print(computer_hand)
            break

        #check if main_pile is empty
        check_bricks(main_pile, discard_pile)
         
        #user's turn
        human_play(user_hand, main_pile, discard_pile)
        print("")
        print("")
          
        #check if user won
        if(check_tower_blaster(user_hand)):
            print("You won! Great Job")
            print(user_hand)
            break

if __name__ == "__main__":
    main()

        
