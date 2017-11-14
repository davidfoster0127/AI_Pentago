
class game:
    def __init__(self):
        self.board = [[['.','.','.'],['.','.','.'],['.','.','.']],
            [['.','.','.'],['.','.','.'],['.','.','.']],
            [['.','.','.'],['.','.','.'],['.','.','.']],
            [['.','.','.'],['.','.','.'],['.','.','.']]]
    
    def play(self, player, quadrant, tile, quadRotate, rotation):
        row = tile//3
        col = tile%3
        if self.isValidMove(quadrant, tile):
            self.placePiece(player, quadrant, tile)
            self.rotate(quadRotate, rotation)
        else:
            print("Invalid play")
    
    def placePiece(self, player, quadrant, tile):
        row = tile//3
        col = tile%3
        if self.isValidMove(quadrant, tile):
            self.board[quadrant][row][col] = player.piece
        else:
            print("Invalid piece placement")

    def rotate(self, quadToRotate, rotation):
        original = self.board[quadToRotate]
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
        self.board[quadToRotate] = rotated

    def checkForGoal(self, player):
        win = False
        lines = []
        #collect horizontal lines (6 lines)
        for i in range(3):
            lines.append(''.join(self.board[0][i]+self.board[1][i]))
            lines.append(''.join(self.board[2][i]+self.board[3][i]))

        #collect vertical lines (6 lines)
        for j in range(3):
            half = self.board[0][0][j]+self.board[0][1][j]+self.board[0][2][j]
            half2 = self.board[2][0][j]+self.board[2][1][j]+self.board[2][2][j]
            lines.append(half+half2)

            halfa = self.board[1][0][j]+self.board[1][1][j]+self.board[1][2][j]
            half2a = self.board[3][0][j]+self.board[3][1][j]+self.board[3][2][j]
            lines.append(halfa+half2a)
        
        #collect diagonal lines
        lines.append(self.board[0][0][0]+self.board[0][1][1]+self.board[0][2][2]+self.board[3][0][0]+self.board[3][1][1]+self.board[3][2][2])
        lines.append(self.board[1][0][2]+self.board[1][1][1]+self.board[1][2][0]+self.board[2][0][2]+self.board[2][1][1]+self.board[2][2][0]) 
        lines.append(self.board[0][0][1]+self.board[0][1][2]+self.board[1][2][0]+self.board[3][0][1]+self.board[3][1][2]) 
        lines.append(self.board[0][1][0]+self.board[0][2][1]+self.board[2][0][2]+self.board[3][1][0]+self.board[3][2][1]) 
        lines.append(self.board[1][0][1]+self.board[1][1][0]+self.board[0][2][2]+self.board[2][0][1]+self.board[2][1][0])
        lines.append(self.board[1][1][2]+self.board[1][2][1]+self.board[3][0][0]+self.board[2][1][2]+self.board[2][2][1])

        for line in lines:
            if player.piece*5 in line:
                win = True
        
        return win

    def isValidMove(self, quadrant, tile):
        valid = False
        if self.board[quadrant][tile//3][tile%3] == '.':
            valid = True
        return valid

    def getPossibleMoves(self):
        moves = []
        for quad in range(4):
            for pos in range(9):
                if self.isValidMove(quad, pos):
                    for quadR in range(4):
                        moves.append([quad, pos, quadR, 'r'])
                        moves.append([quad, pos, quadR, 'l'])
        return moves

    def getLines(self):
        lines = []
        #collect horizontal lines (6 lines)
        for i in range(3):
            lines.append(''.join(self.board[0][i]+self.board[1][i]))
            lines.append(''.join(self.board[2][i]+self.board[3][i]))

        #collect vertical lines (6 lines)
        for j in range(3):
            half = self.board[0][0][j]+self.board[0][1][j]+self.board[0][2][j]
            half2 = self.board[2][0][j]+self.board[2][1][j]+self.board[2][2][j]
            lines.append(half+half2)

            halfa = self.board[1][0][j]+self.board[1][1][j]+self.board[1][2][j]
            half2a = self.board[3][0][j]+self.board[3][1][j]+self.board[3][2][j]
            lines.append(halfa+half2a)
        
        #collect relavent diagonal lines
        lines.append(self.board[0][0][0]+self.board[0][1][1]+self.board[0][2][2]+self.board[3][0][0]+self.board[3][1][1]+self.board[3][2][2])
        lines.append(self.board[1][0][2]+self.board[1][1][1]+self.board[1][2][0]+self.board[2][0][2]+self.board[2][1][1]+self.board[2][2][0]) 
        lines.append(self.board[0][0][1]+self.board[0][1][2]+self.board[1][2][0]+self.board[3][0][1]+self.board[3][1][2]) 
        lines.append(self.board[0][1][0]+self.board[0][2][1]+self.board[2][0][2]+self.board[3][1][0]+self.board[3][2][1]) 
        lines.append(self.board[1][0][1]+self.board[1][1][0]+self.board[0][2][2]+self.board[2][0][1]+self.board[2][1][0])
        lines.append(self.board[1][1][2]+self.board[1][2][1]+self.board[3][0][0]+self.board[2][1][2]+self.board[2][2][1])

        return lines

    def getUtility(self, lines, min, max):
        utility = 0
        scores = [1, 10, 100, 1000]
        for line in lines:
            if max*6 or max*5 in line:
                utility += scores[3]
                pass
            elif max*4 in line:
                utility += scores[2]
                pass
            elif max*3 in line:
                utility += scores[1]
                pass
            elif max*2 in line:
                utility += scores[0]
        for line in lines:
            if min*6 or min*5 in line:
                utility -= scores[3]
                pass
            elif min*4 in line:
                utility -= scores[2]
                pass
            elif min*3 in line:
                utility -= scores[1]
                pass
            elif min*2 in line:
                utility -= scores[0]
        #prioritize the middle pieces
        if utility == 0:
            for i in range(4):
                if self.board[i][1][1] == max:
                    utility += 2
                if self.board[i][1][1] == min:
                    utility -= 2
        
        return utility

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

    def __eq__(self, other):
        return self.board == other.board