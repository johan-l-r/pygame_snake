import pygame as pg

pg.init()

is_running = True

WINDOW_SIZE = 800 # 800x800
MAX_CELLS = 25
CELL_SIZE = WINDOW_SIZE / MAX_CELLS

window = pg.display.set_mode((800, 800))

while is_running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      is_running = False

  # update game

  # draw game
