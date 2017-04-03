"""game tenzi"""
rules = """Tenzi is a quick, fun, one player game.
You start out with 10 dice. The goal of the game is to get all of those dice to be the same number.
First, all ten dice are rolled. You decide which dice you will try to get all ten of.
Then, keep rolling until that happens!
Happy playing!"""
import chance
import time
def returnDiceRoll(x):
    li = []
    while x > 0:
        li.append(chance.oneDie())
        x = x - 1
    return li
def one():
    start = int(time.time())
    myDice = 0
    roun = 1
    while myDice < 10:
        if myDice == 0:
            myDies = returnDiceRoll(10)
            ask = int(input("Your dice are " + str(myDies) + ". Which one do you want to pick?"))
            myDice += myDies.count(ask)
            print("You have",myDice)
        else:
            myDies = returnDiceRoll(10 - myDice)
            gain = myDies.count(ask)
            myDice += gain
            if gain == 1:
                print(ask,'rolled 1 time')
            else:
                print(ask,'rolled',str(gain),'times')
            if myDice == 10:
                print("You won in",roun,'rounds')
            else:
                left = 10 - myDice
                print("You have",left,"left")
                check = input("Ready for next round?")
                roun += 1
    end = int(time.time())
    tTime = end - start
    print("You finished in",tTime,"seconds")
def two():
    start = int(time.time())
    dice1 = 0
    dice2 = 0
    while dice1 < 10 and dice2 < 10:
        if dice1 == 0:
            name1 = input("What is the first player's name?")
            name2 = input("What is the second player's name?")
            roll1 = returnDiceRoll(10)
            ask1 = int(input(name1 + ", your dice roll is " + str(roll1) + ". Which one do you want?"))
            dice1 += roll1.count(ask1)
            print(name1,"has",dice1)
            roll2 = returnDiceRoll(10)
            ask2 = int(input(name2 + ", your dice roll is " + str(roll2) + ". Which one do you want?"))
            dice2 += roll2.count(ask2)
            print(name2,"has",dice2)
        else:
            #player1
            roll1 = returnDiceRoll(10-dice1)
            gain1 = roll1.count(ask1)
            dice1 += gain1
            if gain1 == 1:
                print("For",name1,",",ask1,"rolled 1 time")
            else:
                print("For",name1,",",ask1,"rolled",gain1,"times")
            print(name1,"has",str(10-dice1),'left')
            #player2
            roll2 = returnDiceRoll(10-dice2)
            gain2 = roll2.count(ask2)
            dice2 += gain2
            if gain2 == 1:
                print("For",name2,",",ask2,"rolled 1 time")
            else:
                print("For",name2,",",ask2,"rolled",gain2,"times")
            print(name2,'has',str(10-dice2),'left')
        if dice1 > dice2:
            if dice1 == 10:
                print(name1,"won!")
            else:
                print(name1,"is winning")
                input("Ready for next round?")
        elif dice2 > dice1:
            if dice2 == 10:
                print(name2,"won!")
            else:
                print(name2,"is winning")
                input("Ready for next round?")
                
        else:
            print("You are both tied")
            input("Ready for next round?")
    end = int(time.time())
    total = end - start
    print("the game finished in",total,'seconds')
def main():
    people = int(input("How many people are playing"))
    if people == 1:
        one()
    elif people == 2:
        two()
    else:
        print("Sorry, only one or two people can play.")
        main()
main()
