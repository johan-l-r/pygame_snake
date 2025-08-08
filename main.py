import pygame as pg

pg.init()

is_running = True

WINDOW_SIZE = 800 # 800x800
MAX_CELLS = 25
CELL_SIZE = WINDOW_SIZE / MAX_CELLS

window = pg.display.set_mode((800, 800))

def draw_grid():
  current_cell_color = (0, 0, 0)

  for row in range(MAX_CELLS):
    for col in range(MAX_CELLS):
      cell = pg.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE)

      # create chess board pattern
      if (row + col) % 2 == 0:
        current_cell_color = (20, 20, 20)
      else:
        current_cell_color = (0, 0, 0)

      pg.draw.rect(window, current_cell_color, cell)

while is_running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      is_running = False

  # update game

  # draw game
  draw_grid()

  pg.display.flip()
