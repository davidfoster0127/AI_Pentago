


class game:
    def __init__(self):
        self.board = [[['.','.','.'],['.','.','.'],['.','.','.']],
            [['.','.','.'],['.','.','.'],['.','.','.']],
            [['.','.','.'],['.','.','.'],['.','.','.']],
            [['.','.','.'],['.','.','.'],['.','.','.']]]
    
    def __str__(self):
        boardstring = ''
        line = "+-------+-------+\n"
        boardstring+=line
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[0][0][num]
        boardstring+=' '
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[1][0][num]
        boardstring+=' '
        boardstring+="|\n|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[0][1][num]
        boardstring+=' '
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[1][1][num]
        boardstring+=' '
        boardstring+="|\n|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[0][2][num]
        boardstring+=' '
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[1][2][num]
        boardstring+=' '
        boardstring+="|\n"
        
        boardstring+=line
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[2][0][num]
        boardstring+=' '
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[3][0][num]
        boardstring+=' '
        boardstring+="|\n|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[2][1][num]
        boardstring+=' '
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[3][1][num]
        boardstring+=' '
        boardstring+="|\n|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[2][2][num]
        boardstring+=' '
        boardstring+="|"
        for num in range(3):
            boardstring+=' '
            boardstring+=self.board[3][2][num]
        boardstring+=' '
        boardstring+="|\n"
        boardstring+=line
        return boardstring

class player:
    def __init__(self, piece):
        self.piece = piece

def rotate(game, quadToRotate, rotation):
    original = game.board[quadToRotate]
    rotated = [['.','.','.'],['.','.','.'],['.','.','.']]
    if rotation.lower() == 'r':
        rotated[0][0] = original[2][0]
        rotated[0][1] = original[1][0]
        rotated[0][2] = original[0][0]
        rotated[1][0] = original[2][1]
        rotated[1][1] = original[1][1]
        rotated[1][2] = original[0][1]
        rotated[2][0] = original[2][2]
        rotated[2][1] = original[1][2]
        rotated[2][2] = original[0][2]
    elif rotation.lower() == 'l':
        rotated[0][0] = original[0][2]
        rotated[0][1] = original[1][2]
        rotated[0][2] = original[2][2]
        rotated[1][0] = original[0][1]
        rotated[1][1] = original[1][1]
        rotated[1][2] = original[2][1]
        rotated[2][0] = original[0][0]
        rotated[2][1] = original[1][0]
        rotated[2][2] = original[2][0]
    game.board[quadToRotate] = rotated

def play(game, player, quadrant, tile, quadRotate, rotation):
    col = tile % 3
    row = tile//3

    game.board[quadrant][row][col] = player.piece
    rotate(game, quadRotate, rotation)



#main method
def main():
    """the main method of the program"""
    print("hello")
    player1 = player('1')
    player2 = player('2')
    board = game()
    print(board)
    play(board, player1, 0, 1, 0, 'r')
    play(board, player2, 2, 5, 2, 'l')
    print(board)

if __name__ == "__main__":
    main()