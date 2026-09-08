from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [None, None, None, None, None, None, None, None, None]
        self.current = "X"
        self.winner = None
        self.winning_line = None
        self.draw = False
        self.finished = False

    def check_winner(self):
        winning_lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for line in winning_lines:
            if (self.board[line[0]] == self.board[line[1]] == self.board[line[2]]) and (self.board[line[0]] == "X" and self.board[line[1]] == "X" and self.board[line[2]] == "X"):
                self.winner = "X"
                self.winning_line = line
                self.draw = False
                self.finished = True
            elif (self.board[line[0]] == self.board[line[1]] == self.board[line[2]]) and (self.board[line[0]] == "O" and self.board[line[1]] == "O" and self.board[line[2]] == "O"):
                self.winner = "O"
                self.winning_line = line
                self.draw = False
                self.finished = True

    def move(self):
        self.check_winner()
        if all(i is not None for i in self.board):
            self.winner = None
            self.winning_line = None
            self.draw = True
            self.finished = True



game = Game()

@app.get("/game")
def get_game():
    return {
        "board": game.board,
        "current": game.current,
        "winner": game.winner,
        "winning_line": game.winning_line,
        "draw": game.draw,
        "finished": game.finished
    }

@app.post("/game")
def post_game():
    game.reset()

    return {
        "board": game.board,
        "current": game.current,
        "winner": game.winner,
        "winning_line": game.winning_line,
        "draw": game.draw,
        "finished": game.finished
    }

@app.post("/game/move")
def game_move(index: int = Body(..., embed=True)):

    if isinstance(index, int) == False:
        raise HTTPException(status_code=422, detail="Index is not an integer")
    if index < 0 or index > 8:
        raise HTTPException(status_code=422, detail="Index out of range")
    if game.finished == True:
        raise HTTPException(status_code=409, detail="Game has ended")
    if game.board[index] == "X" or game.board[index] == "O":
        raise HTTPException(status_code=409, detail="Cell is already taken")


    game.board[index] = game.current

    game.move()

    if game.current == "X":
        game.current = "O"
    else:
        game.current = "X"
    return {
        "board": game.board,
        "current": game.current,
        "winner": game.winner,
        "winning_line": game.winning_line,
        "draw": game.draw,
        "finished": game.finished
    }