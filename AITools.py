from Board import Board
import copy

class AITools:
    def __init__(self):
        pass

    def getMove(self, board):
        
        boardList = self.getMoveOutcomes(board)
        if self.isGridlock(board, boardList): return 4
        
        scoreList = []

        for new in boardList:
            scoreList.append(self.calculateScore(board, new))

        return scoreList.index(max(scoreList))

    def calculateScore(self, oldBoard: Board, newBoard: Board):

        if oldBoard.state == newBoard.state: return -5000

        score = 0

        BIGGEST_IN_CORNER = 2000
        HOME_ROWS_DECREASE = 50

        # award points for score increase
        score += newBoard.score - oldBoard.score

        # check if the largest tile in newBoard is on a corner
        largestTile = 0
        largestTilePos = (0, 0)
        for row in range(4):
            for col in range(4):
                if newBoard.state[row][col] > largestTile:
                    largestTile = newBoard.state[row][col]
                    largestTilePos = (row, col)
        if largestTilePos == (0, 0):
            score += BIGGEST_IN_CORNER

            if largestTilePos == (0,0):
                if newBoard.state[0][0]/2 == newBoard.state[1][0]:
                    score += HOME_ROWS_DECREASE
                    if newBoard.state[1][0]/2 == newBoard.state[2][0]:
                        score += HOME_ROWS_DECREASE
                        if newBoard.state[2][0]/2 == newBoard.state[3][0]:
                            score += HOME_ROWS_DECREASE
                if newBoard.state[0][0]/2 == newBoard.state[0][1]:
                    score += HOME_ROWS_DECREASE
                    if newBoard.state[0][1]/2 == newBoard.state[0][2]:
                        score += HOME_ROWS_DECREASE
                        if newBoard.state[0][2]/2 == newBoard.state[0][3]:
                            score += HOME_ROWS_DECREASE

        return score

    def getMoveOutcomes(self, board: Board):

        boardUp = copy.deepcopy(board)
        boardDown = copy.deepcopy(board)
        boardLeft = copy.deepcopy(board)
        boardRight = copy.deepcopy(board)

        boardUp.slide_up()
        boardDown.slide_down()
        boardLeft.slide_left()
        boardRight.slide_right()

        return [boardUp, boardDown, boardLeft, boardRight]
    
    def isGridlock(self, originalBoard: Board, boardList: [Board]):
        for board in boardList:
            if board.state != originalBoard.state:
                return False
        return True

tester = AITools()

board = Board()
board.state =  [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [2, 0, 0, 0],
                [2, 0, 0, 0]]

