from readBingoFromFile import calls, board

class Board:
    def __init__(self, board):
        self.ints = [int(space) for space in board.split()]
        self.leftOver = set(self.ints)
        self.won = False

    @property
    def hasWon(self):
        for x in range(5):
            for y in range(5):
                #check row
                if self.ints[x * 5 + y] in self.leftOver:
                    break
            else:
                return True
            for y in range(5):
                #check column
                if self.ints[x + 5 * y] in self.leftOver:
                    break
            else: 
                return True
        else:
            return False


integerBoards = [Board(space) for space in board]

def getWinner():
    # keep track of last winner
    prevWinnerResult = -1
    for call in calls:
        for board in integerBoards:
            board.leftOver.discard(call)
        for ind, board in enumerate(integerBoards):
            if not board.won and board.hasWon:
                prevWinnerResult = sum(board.leftOver) * call
                board.won = True
    return prevWinnerResult

print(getWinner())