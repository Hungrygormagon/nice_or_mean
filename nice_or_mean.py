#
# Python: 3.8.2
#
# Author: Steven J. Carney
#
# Purpose: Developing first Python program in The Tech Academy Python Course
#
# Name: Nice or Mean Game
#
#
#
#
#
#
#

def start(nice = 0, mean = 0, name = ""): 
    #Gets users name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        check if this is a new game or not,
        if it is new, get the users name.
        if it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not have this user's name,
    #then they are a new player and we need their name.
    if name !="":
        print("\nThank you for playing again, {}!".format(name))
    else: 
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>> ").capitalize()
                if name !="":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted \nBy several different people. \n\nYou can choose to be nice, or mean")
                    print("But at the end of the game your fate \nWill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop=True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice, \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1)
            stop= False
        if pick == "m":
            print('\nThe stranger glasres at you \nmenacingly and storms off...')
            mean = (mean + 1)
            stop=False
    score(nice, mean, name) #Passes the users name and scores to score()

def show_score(nice, mean, name):
    print("\n{}, your current total is: \n({}, Nice) ({}, Mean)".format(name,nice,mean))

def score(nice, mean, name):
    #Score function is being passed the values
    if nice > 2: #if codition is valid, call win function passing in the variables
        win(nice, mean, name)
    if mean > 2: #calls lose function if valie
        lose(nice, mean, name)
    else: #goes back to nice_mean if neither are valid
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print("\nNice job {}, you win! \nEveryone loves you, and you've made lots of friends along the way!".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    again(nice, mean, name) 

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':/n>>>")

def reset(nice, mean, name): #resetting scores, but not name as this is the same player
    nice = 0
    mean = 0
    start(nice, mean, name)

if __name__ == "__main__":
    start()
