#Author: Islam Hani Awad
#Job: Student at FCAI faculty, Cairo University
#About: Num-21 Game
#Description: You can play this game with your friend or with computer. Nim-21 game, The game starts by having 21 coins. Player take turns to take some of the coins. Each player takes 1, 2, or 3 coins. The player who takes the last coin loses.


from random import randint

class Input(object):
    def choose(Self):
        print("\nPlease Enter Choice(^-^)\n")
        print("[1] Player  Vs  Computer.\n")
        print("[2] Player1 Vs  Player2.\n")
        print("[3] Game Description.\n")
        print("[4] Exit.\n")

        choice = int(input("\nWait For Choice: "))
        return choice
    
    def description(Self):
        print("\nNim-21 game. The game starts by having 21 coins. Player take turns to take some of the coins. Each player takes 1, 2, or 3 coins. The player who takes the last coin loses.\n")
        print("\n -------------------------------------------------------------- \n")
        
#----------------------------------------------------------------------------------------------------------------------------------------

class Player(object):
    def takeCoins(Self, name, coins):
        print("\n> Game Coins: ", coins)
        while True:
            try:
                noCoins = int(input(name+" play: "))
                if(1<=noCoins<=3):
                    coins = coins - noCoins
                    return coins

            except:
                print("Please enter a number")

#----------------------------------------------------------------------------------------------------------------------------------------

class Computer(object):
    def takeCoins(Self, coins):
        print("\n> Game Coins: ", coins)
        noCoins = randint(1, 3)
        print("Computer: ", noCoins)
        coins = coins - noCoins
        return coins
        
#----------------------------------------------------------------------------------------------------------------------------------------

class Game(object):
    def play(Self, choice):
            coins = 21
            if(choice == 1):
                player = Player()
                computer = Computer()
                while(coins>0):
                    coins = player.takeCoins("Player", coins)
                    if(coins <= 0):
                        print("\nPlayer IS LOSE...\n")
                        break
                                
                    coins = computer.takeCoins(coins)
                    if(coins <= 0):
                        print("\nPlayer IS WIN...\n")
                        break
                    
            elif(choice == 2):
                player1 = Player()
                player2 = Player()
                while(coins>0):
                    coins = player1.takeCoins("Player1", coins)
                    if(coins <= 0):
                        print("\nPlayer2 IS WIN...\n")
                        break
                                
                    coins = player2.takeCoins("Player2", coins)
                    if(coins <= 0):
                        print("\nPlayer1 IS WIN...\n")
                        break
        
#-----------------------------------------------------------#MAIN#-----------------------------------------------------------------------

while True:
    gm = Game()
    try:
        inp = Input()
        choice = inp.choose()

        if(choice == 3):
            inp.description()

        elif(choice == 4):
            print("\n.... Exiting ....\n")
            break

        else:
            gm.play(choice)

    except:
        print("Please enter a number")
