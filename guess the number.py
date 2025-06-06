import random
import time
number=random.randint(1,100)
def intro():
    print("please enter your name: ")
    global name
    name=input()
    print(name + ", we are going to play a game. I'm going to guess a number between 1 to 100")
    if (number%2==0):
        x='even'
    else:
        x='odd'
    print("\nthis is an {} number".format(x))
    time.sleep(.5)
    print("go ahead. guess")
def pick():
    guessesTaken=0
    while guessesTaken<6:
        time.sleep(0.25)
        enter=input("guess: ")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                       print("the guess that you have entered is too low")
                    if guess>number:
                       print("the guess of the number that you have entered is too high")
                    if guess!=number:
                       time.sleep(.5)
                       print("try again")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("that numbe is not in the range")
                time.sleep(.25)
                print("please enter a number between 1 and 100")
        except:
            print('I dont think that "+enter+" is a number')
    if guess == number:
        guessesTaken=str(guessesTaken)
        print('good job, {} you guessed my number in {} guesses'.format(name,guessesTaken))
    if guess !=number:
        print("nope. The number i was thinking of was" +str (number))
playagain='yes'
while playagain=='yes' or playagain=='y' or playagain=='Yes':
    intro()
    pick()
    print("do you want to play again?")
    playagain=input()