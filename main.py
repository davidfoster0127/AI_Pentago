
import pentago
import re
import random
import AI


class player:
    def __init__(self, piece):
        self.piece = piece

if __name__ == "__main__":
    human = player('')
    computer = player('')
    opponent = AI.player()
    board = pentago.game()


    while human.piece not in ['w', 'b']:
        human.piece = input('Choose Player Color (w or b): ')
    if human.piece == 'w': 
        computer.piece = 'b'
    else: computer.piece = 'w'

    opponent.mincolor = human.piece
    opponent.maxcolor = computer.piece

    print(board)
    board.play(human, 0, 1, 0, 'r')
    board.play(computer, 2, 5, 2, 'l')
    board.play(human, 0, 2, 0, 'l')
    board.play(human, 0, 2, 3, 'r')
    board.play(human, 1, 0, 3, 'r')
    board.play(human, 1, 1, 3, 'r')
    print(board)
    print(board.checkForGoal(human))
    