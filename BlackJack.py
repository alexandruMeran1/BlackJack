import random
import os

os.system( "cls" )


def draw( ) :
    cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
    return random.choice( cards )


if (input( "Do you want to play BlackJack ? Type yes or no \n" ) == "yes") :
    play = True
else :
    play = False

while (play) :
    os.system( "cls" )
    player = []
    dealer = []
    for _ in range( 2 ) :
        player.append( draw( ) )
        dealer.append( draw( ) )

    if (player[0] == 11 and player[1] == 11) :
        player[0] = 1
    if (dealer[0] == 11 and dealer[1] == 11) :
        dealer[0] = 1

    print( f"You have :{player} ({sum( player )})\n Dealer has :[{dealer[0]}]" )
    if (sum( player ) == 21) :
        print( f"Congrats you have a BlackJack {player}" )
    else :
        while sum( player ) < 21 :
            if (input( "Do you want to draw another card ? Type yes or no \n" ) == "yes") :
                os.system( "cls" )
                player.append( draw( ) )
                if (player.count( 11 ) and sum( player ) > 21) :
                    player[player.index( 11 )] = 1
                print( f"You have {player} ({sum( player )}) \n Dealer has [{dealer[0]}] " )
            else :
                break

    if (sum( player ) > 21) :
        print( "Busted!" )

    while sum( dealer ) <= 16 :
        dealer.append( draw( ) )
        if (dealer.count( 11 ) and sum( dealer ) > 21) :
            dealer[dealer.index( 11 )] = 1

    print( f"Dealer has {dealer} ({sum( dealer )})" )

    if (sum( dealer ) > 21 and sum( player ) < 22) :
        print( "Dealer busted . You Won!" )
    elif sum( player ) < 22 and sum( dealer ) < 22 and sum( player ) == sum( dealer ) :
        print( "Draw" )
    elif (sum( player ) > 21) :
        print( "You lost" )
    elif sum( dealer ) < sum( player ) :
        print( "You won !" )
    else :
        print( "You lost" )

    if input( "Do you want to play again ? Type yes or no\n" ) != "yes" :
        play = False
        os.system( "cls" )
        print( "\n See you next time ! :D" )
    else :
        play = True
