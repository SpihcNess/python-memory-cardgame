from numpy import *
from carddraw import *

#création plateau de jeu de cartes et plateau visible
hiddenPlateau = array([deck[0:13],deck[13:26],deck[26:39],deck[39:52]])
plateau = array([('##','##','##','##','##','##','##','##','##','##','##','##','##','00'),('##','##','##','##','##','##','##','##','##','##','##','##','##','01'),('##','##','##','##','##','##','##','##','##','##','##','##','##','02'),('##','##','##','##','##','##','##','##','##','##','##','##','##','03'),('00','01','02','03','04','05','06','07','08','09','10','11','12','00')])

i=0
good=0

#jeu
def playMemory():
    
    print(plateau)
    global i
    global good
    a=0
    b=0
    c=0
    d=0

    while good<26:
        if i < 5:
            try :
                a, b = [int(x) for x in input('''Press V if you want to quit.

Put the coordinates of a still available card, separated by a space: ''').split()]
            except ValueError :
                o=input('Do you still want to play Memory ? (y/n)')
                if o == 'y' or o =='Y':
                    i =i +1
                    playMemory()
                else:
                    print('THEN GO BACK FROM WHERE YOU CAME FROM !')
                    from beginning import Game_Choice
                    Game_Choice()
            if a not in [0, 1, 2, 3] or b not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] :
                print('Please enter valid coordinates.')
                i = i + 1
                playMemory()
            else:
                card1 = hiddenPlateau[a][b]
                print('You picked ' + card1)
                try :
                    c, d = [int(x) for x in input('Put the coordinates of a still available card, separated by a space: ').split()]
                except ValueError :
                    print('Please enter valid coordinates.')
                    i =i +1
                    playMemory()
                if c not in [0, 1, 2, 3] or d not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] :
                    print('Please enter valid coordinates.')
                    i = i + 1
                    playMemory()
                else:
                    card2 = hiddenPlateau[c][d]
                    print('You picked ' + card2)
                    print(card1)
                    print(card2)
                    if (('♦' in card2 and '♥' in card1) or ('♣' in card2 and '♠' in card1) or ('♥' in card2 and '♦' in card1) or ('♠' in card2 and '♣' in card1)) and (('A' in card2 and 'A' in card1) or ('2' in card2 and '2' in card1) or ('3' in card2 and '3' in card1) or ('4' in card2 and '4' in card1) or ('5' in card2 and '5' in card1) or ('6' in card2 and '6' in card1) or ('7' in card2 and '7' in card1)or ('8' in card2 and '8' in card1) or ('9' in card2 and '9' in card1) or ('10' in card2 and '10' in card1) or ('J' in card2 and 'J' in card1) or ('Q' in card2 and 'Q' in card1) or ('K' in card2 and 'K' in card1)):
                        good = good + 1 
                        print('''OMG ! You got a couple !

You now have ''' + str(good) + ''' point(s).''')
                        plateau[a][b]='  '
                        plateau[c][d]='  '
                        playMemory()
                    else:
                        print('Wrong cards... try again!')
                        playMemory()
        else:
            print("Nah, I give up. You didn't listen to me. I'm sad. (ಥ﹏ಥ) ")
            endMemory()
    endMemory()
    
#fin du jeu (rejouer et autre jeu)
    
def endMemory():
    global z
    global w
    global i
    global good
    
    if "##" in plateau:
        z=input('''You lose !
Either you put more than one time a couple (be careful !), either you wanted to cheat !
Cheathing is bad !

Press G to play again
Press N to play another game

''')
        if z=='G' or z=='g':
            i=0
            good=0
            playMemory()
        elif z=='N' or z=='n':
            i=0
            good=0
            from beginning import Game_Choice
            Game_Choice()
        else:
            endMemory()
    else:
        w=input('''Congrats, you won ! ۹(ÒہÓ)۶

You're what they call a genius (like in Aladdin you know). I'm glad I met you. (ಥ﹏ಥ)
What would you want to do ?

Press G to play again
Press N to play another game
            
''')
        if w=='G' or w=='g':
            i=0
            good=0
            playMemory()
        elif w=='N' or w=='n':
            i=0
            good=0
            from beginning import Game_Choice
            Game_Choice()
        else:
            endMemory()

playMemory()
