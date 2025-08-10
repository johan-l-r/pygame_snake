import pygame as pg
import random

pg.init()

is_running = True

WINDOW_SIZE = 800 # 800x800
MAX_CELLS = 25
CELL_SIZE = WINDOW_SIZE / MAX_CELLS

# [0] = x [1] = y
movement_direction = [1, 0]

snake_x_pos = 12 * CELL_SIZE
snake_y_pos = 12 * CELL_SIZE

move_timer = 0
move_time = 5

window = pg.display.set_mode((800, 800))

snake_head = pg.Rect(snake_x_pos, snake_y_pos, CELL_SIZE, CELL_SIZE)
apple = pg.Rect(
  random.randint(0, MAX_CELLS) * CELL_SIZE,
  random.randint(0, MAX_CELLS) * CELL_SIZE,
  CELL_SIZE, CELL_SIZE
)

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
    if event.type == pg.KEYDOWN:
      if (event.key == pg.K_w or event.key == pg.K_UP) and movement_direction[1] != 1:
        movement_direction = [0, -1]
      if (event.key == pg.K_s or event.key == pg.K_DOWN) and movement_direction[1] != -1:
        movement_direction = [0, 1]
      if (event.key == pg.K_a or event.key == pg.K_LEFT) and movement_direction[0] != 1:
        movement_direction = [-1, 0]
      if (event.key == pg.K_d or event.key == pg.K_RIGHT) and movement_direction[0] != -1:
        movement_direction = [1, 0]

  # update game
  move_timer += 0.1

  if move_timer >= move_time:
    snake_head.x += int(movement_direction[0] * CELL_SIZE)
    snake_head.y += int(movement_direction[1] * CELL_SIZE)

    move_timer = 0

  if snake_head.colliderect(apple):
    move_time -= 0.01
    apple.x = int(random.randint(0, MAX_CELLS - 1) * CELL_SIZE)
    apple.y = int(random.randint(0, MAX_CELLS - 1) * CELL_SIZE)

  # draw game
  draw_grid()
  pg.draw.rect(window, (255, 255, 255), snake_head)
  pg.draw.rect(window, (255, 0, 0), apple)

  pg.display.flip()
