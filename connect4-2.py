
import random as r
import pygame as pg


pg.init()

board_dimensions = (7, 6)
token_size = 100
gap = 20

top_of_board = 2 * (token_size + gap)

screen_width = (board_dimensions[0]) * (token_size + gap) + gap
screen_height = (board_dimensions[1]) * \
    (token_size + gap) + gap + top_of_board


board_state = [[0]*board_dimensions[1] for i in range(board_dimensions[0])]
# 0 is empty, 1 is red, 2 is yellow

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 84, 255)
GREEN = (95, 199, 87)

colors = (WHITE, RED, YELLOW)

turn = 0
total_turns = board_dimensions[0] * board_dimensions[1]
# 0 is player1, 1 is player2


def clamp(min_v, max_v, val):
    return max(min_v, min(max_v, val))


def drawBoard():
    pg.draw.rect(window, BLUE, pg.Rect(0, top_of_board, screen_width,
                 (board_dimensions[1]) * (token_size+gap)+gap))


def drawBoardState():
    for i in range(board_dimensions[0]):
        for j in range(board_dimensions[1]):
            color = colors[board_state[i][j]]
            centerX = int(gap * (i+1) + token_size/2 + (token_size * i))
            centerY = int(gap * (j+1) + token_size/2 +
                          top_of_board + token_size * j)
            center = (centerX, centerY)
            pg.draw.circle(window, color, center, int(token_size/2))


def drawPlayerToken():
    color = colors[turn+1]
    center = curPos
    pg.draw.circle(window, color, center, int(token_size/2))


def dropToken():
    global turn, board_state, total_turns, run
    dropCol = (int((curPos[0] / (token_size + gap))))
    # print(dropCol)

    goodDrop, dropRow = tokenFall(dropCol)
    if goodDrop:
        turn = (turn + 1) % 2
        total_turns -= 1

    # Check if player won
    if goodDrop:
        if checkWin(dropCol, dropRow):
            print('Winner')

    # Check if board full
    if total_turns == 0:
        run = False
        print('Draw!')


def tokenFall(col):
    for i in range(board_dimensions[1]-1, -1, -1):
        if board_state[col][i] == 0:
            board_state[col][i] = turn + 1
            return True, i
    return False, -1


def checkWin(col, row):
    curToken = board_state[col][row]
    # Check verticality
    try:
        if board_state[col][row+1] == curToken and board_state[col][row+2] == curToken and board_state[col][row+3] == curToken:
            return True
    except:
        pass

    for i in range(0, -4, -1):
        # Check horizontality
        try:
            if board_state[col+i][row] == curToken and board_state[col+i+1][row] == curToken and board_state[col+i+2][row] == curToken and board_state[col+i+3][row] == curToken:
                return True
        except:
            pass

        # Check left diagonally
        try:
            if board_state[col+i][row+i] == curToken and board_state[col+i+1][row+i+1] == curToken and board_state[col+i+2][row+i+2] == curToken and board_state[col+i+3][row+i+3] == curToken:
                return True
        except:
            pass
        # Check right diagonally
        try:
            if board_state[col-i][row+i] == curToken and board_state[col-i-1][row+i+1] == curToken and board_state[col-i-2][row+i+2] == curToken and board_state[col-i-3][row+i+3] == curToken:
                return True
        except:
            pass

    return False


window = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption("Connect 4")


run = True
curPos = [0, int(top_of_board - gap - token_size/2)]
while(run):
    pg.time.delay(int(1000/60))

    window.fill(GREEN)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            dropToken()
        if event.type == pg.MOUSEMOTION:
            curPos[0] = clamp(
                int(gap + token_size/2), screen_width - int(gap + token_size/2), event.pos[0])

        # if event.type == pg.KEYDOWN:
        #     keys = pg.key.get_pressed()
        #     if keys[pg.K_SPACE]:
        #         run_simulation = not run_simulation
        #     if keys[pg.K_r]:
        #         generateRandomGrid()
        #     if keys[pg.K_c]:
        #         grid = [[0]*pixel_count[1] for i in range(pixel_count[0])]
        #     if keys[pg.K_s]:
        #         updateGrid()

    drawBoard()
    drawBoardState()
    drawPlayerToken()

    # pg.draw.rect(window, (0, 0, 0), pg.Rect(100, 200, 300, 50))

    pg.display.update()
