"""
Author: David Foster
Date: 11/12/2017
"""

import pentago
import re
import random
import AI

#changes move format to match specs
def formatMoveStr(move):
    s = ''
    quad = str(move[0]+1)
    tile = str(move[1]+1)
    quadtorotate = str(move[2]+1)
    rotation = move[3]
    s = s.join(quad+'/'+tile+' '+quadtorotate+rotation.upper())
    return s

if __name__ == "__main__":
    human = ''
    computer = ''
    opponent = AI.agent()
    game = pentago.game()
    nextTurn = ''
    movestring = ''
    humanwin = False
    computerwin = False

    outfile = open('Output.txt', 'w')
    
    #choose player pieces (w or b)
    while human not in ['w', 'b']:
        human = input('Choose Player Color (w or b): ')
    if human == 'w': 
        computer = 'b'
    else: computer = 'w'

    #set ai min and max colors
    opponent.mincolor = human
    opponent.maxcolor = computer
    
    #randomly assign who goes first
    nextTurn = [human, computer][random.randint(0,1)]
    if nextTurn is human: 
        print('Player Goes First!')
    else: 
        print('Computer Goes First')

    #initial output file writing
    outfile.write('Player color: ' + human + '\n')
    outfile.write('Computer color: ' + computer + '\n')
    outfile.write('Player to move first: ' + nextTurn + '\n')
    outfile.write(str(game))
    print(game)

    #main game loop that exits when humanwin or computerwin = true
    try:
        while(True):
            if nextTurn is human:
                validmove = False

                #loop for checking valid move format
                while not validmove:
                    movestring = input('Enter Move (%s): ' %human)
                    validmove = re.match('^[1-4]\/[1-9] [1-4][RrLl]', movestring)
                    if validmove: 
                        move = [int(movestring[0]) - 1, int(movestring[2]) - 1, int(movestring[4]) - 1, movestring[5]]
                        validmove = game.isValidMove(move[0], move[1])
                    if not validmove:
                        print('Invalid move, try again')
                        print('Please use the format [1-4]/[1-9] [1-4]/[L or R] (Quadrant/Tile QuadrantToRotate/Rotation)')
      
            else:
                print("Computer's Turn...")
                move = opponent.getMove(game)
            
            #place the tile and check for win
            game.placePiece(nextTurn, move[0], move[1])
            humanwin = game.checkForGoal(human)
            computerwin = game.checkForGoal(computer)
            if humanwin or computerwin: break
            
            #rotate the quadrant and check for win
            game.rotate(move[2], move[3])
            humanwin = game.checkForGoal(human)
            computerwin = game.checkForGoal(computer)
            if humanwin or computerwin: break
            
            #check for a tie
            if all('.' not in line for line in game.getLines()):
                humanwin = computerwin = True
                break

            print(formatMoveStr(move))
            print(game)

            outfile.write(formatMoveStr(move) + '\n')
            outfile.write(str(game) + '\n')
            
            #swap turns
            if nextTurn is human: 
                nextTurn = computer
            else: 
                nextTurn = human
        
        #print final move and board state to console and output.txt
        print(formatMoveStr(move))
        print(game)
        outfile.write(formatMoveStr(move) + '\n')
        outfile.write(str(game))
        
        #determine who the winner was
        if humanwin and not computerwin: 
            print('Player Wins!')
        elif computerwin and not humanwin: 
            print('Computer Wins!')
        else: 
            print('Tie Game!')
    finally:
        outfile.close()
    