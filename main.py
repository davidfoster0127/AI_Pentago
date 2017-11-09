


class game:

    def __init__(self):
        self.board = []
        self.quarterTile = [['.','.','.'],['.','.','.'],['.','.','.']]
        for num in range(4):
            self.board.append(self.quarterTile)
    
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
    temp = game.board[quadToRotate]
    temp2 = []
    if rotation.lower() == 'r':
        temp2[0][0] = temp[2][0]
        temp2[0][1] = temp[1][0]
        temp2[0][2] = temp[0][0]
        temp2[1][0] = temp[2][1]
        temp2[1][1] = temp[1][1]
        temp2[1][2] = temp[0][1]
        temp2[2][0] = temp[2][2]
        temp2[2][1] = temp[1][2]
        temp2[2][2] = temp[0][2]
    elif rotation.lower() == 'l':
        temp2[0][0] = temp[0][2]
        temp2[0][1] = temp[1][2]
        temp2[0][2] = temp[2][2]
        temp2[1][0] = temp[0][1]
        temp2[1][1] = temp[1][1]
        temp2[1][2] = temp[2][1]
        temp2[2][0] = temp[0][0]
        temp2[2][1] = temp[1][0]
        temp2[2][2] = temp[2][0]
    game.board[quadToRotate] = temp2

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
    print(board)

if __name__ == "__main__":
    main()