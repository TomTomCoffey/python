import pygame as pg
import random as r

pg.init()

pixel_size = 5
pixel_count = (int(1920/10), int(1080/10))

screen_width = pixel_size * pixel_count[0]
screen_height = pixel_size * pixel_count[1]

run_simulation = False

live_color = (0, 0, 0)
dead_color = (255, 255, 255)

grid = [[0]*pixel_count[1] for i in range(pixel_count[0])]


def clamp(min_v, max_v, val):
    return max(min_v, min(max_v, val))


def generateRandomGrid():
    global grid

    fillPercentage = 0.5

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if r.random() < fillPercentage:
                grid[i][j] = 1


def updateGrid():
    global grid, pixel_count

    # print(grid)
    gridCopy = [[0]*pixel_count[1] for i in range(pixel_count[0])]

    # Some cool [survives, born]
    # [[1], [1]] - Recursive Structure
    # [[2, 3], [3]] - Default Conways GOL

    survives = [1, 1]
    born = [2]

    # Any live cell with two or three live neighbours survives.
    # Any dead cell with three live neighbours becomes a live cell.
    # All other live cells die in the next generation. Similarly, all other dead cells stay dead.

    for i in range(0, len(grid)):
        for j in range(len(grid[i])):
            cur_count = n_count(i, j)
            if (cur_count in survives and grid[i][j] == 1) or (cur_count in born and grid[i][j] == 0):
                gridCopy[i][j] = 1

    grid = gridCopy.copy()

# Write a function to count the number of neighbors around a given cell with the parameters (x, y)


def n_count(x, y):
    global grid
    # print(x, y, pixel_count)
    count = -grid[x][y]
    # grid[y][x]
    # count += grid[y][x]
    # 0 1 2 3 4 5
    # 1 0 0 1 0 1
    # 2 1 0 1 0 1
    # 3 1 1 1 0 1
    # 4 1 0 0 1 1
    # 5 1 0 1 0 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                count += grid[i + x][j + y]
            except:
                pass

    return count


def drawGrid():
    global grid, window

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pg.draw.rect(window, live_color, pg.Rect(
                    i*pixel_size, j*pixel_size, pixel_size, pixel_size))


# generateRandomGrid()

# print(grid)

window = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption("Conway's GOL")

drawGrid()

# grid[40][20] = 1

run = True
curPos = [0, 0]
while(run):
    pg.time.delay(100)

    window.fill(dead_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            curPos[0] = event.pos[0]
            curPos[1] = event.pos[1]
            # Given curPos, swap the value of a given pixel in 'grid'
            grid[int(curPos[0]/pixel_size)][int(curPos[1]/pixel_size)] = (
                grid[int(curPos[0]/pixel_size)][int(curPos[1]/pixel_size)] + 1) % 2

        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                run_simulation = not run_simulation
            if keys[pg.K_r]:
                generateRandomGrid()
            if keys[pg.K_c]:
                grid = [[0]*pixel_count[1] for i in range(pixel_count[0])]
            if keys[pg.K_s]:
                updateGrid()

    if run_simulation:
        updateGrid()
    drawGrid()

    # print(n_count(40, 20))

    # pg.draw.rect(window, (0, 0, 0), pg.Rect(100, 200, 300, 50))

    pg.display.update()
