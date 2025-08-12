import pygame as pg
import random

pg.init()

is_running = True

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 896

SCORE_BAR_WIDTH = WINDOW_WIDTH
SCORE_BAR_HEIGHT = 96

GRID_SIZE = WINDOW_WIDTH

MAX_CELLS = 25
CELL_SIZE = GRID_SIZE / MAX_CELLS

snake_x_pos = 12 * CELL_SIZE
snake_y_pos = 12 * CELL_SIZE

score = 0
move_timer = 0
move_time = 5

# [0] = x [1] = y
movement_direction = [1, 0]

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

snake_head = pg.Rect(snake_x_pos, snake_y_pos, CELL_SIZE, CELL_SIZE)

snake_body = [snake_head]

apple = pg.Rect(
  random.randint(0, MAX_CELLS) * CELL_SIZE,
  random.randint(0, MAX_CELLS) * CELL_SIZE,
  CELL_SIZE, CELL_SIZE
)

font = pg.font.Font("./assets/fonts/Pixeled.ttf", 30)
font_surface = font.render("Score: " + str(score), True, (255, 255, 255))

score_surface = pg.Surface((SCORE_BAR_WIDTH, SCORE_BAR_HEIGHT))

def draw_grid():
  current_cell_color = (0, 0, 0)

  for row in range(MAX_CELLS):
    for col in range(MAX_CELLS):
      cell = pg.Rect(row * CELL_SIZE, SCORE_BAR_HEIGHT + col * CELL_SIZE, CELL_SIZE, CELL_SIZE)

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

  window.fill((0, 0, 0))

  # update game
  move_timer += 0.1

  if move_timer >= move_time:
    for i in range(0, len(snake_body) - 1, 1):
      snake_body[i].x = snake_body[i + 1].x
      snake_body[i].y = snake_body[i + 1].y

    snake_head.x += int(movement_direction[0] * CELL_SIZE)
    snake_head.y += int(movement_direction[1] * CELL_SIZE)

    move_timer = 0

  # apple collision
  if snake_head.colliderect(apple):
    move_time -= 0.01

    apple.x = int(random.randint(0, MAX_CELLS - 1) * CELL_SIZE)
    apple.y = int(random.randint(0, MAX_CELLS - 1) * CELL_SIZE)

    score += 1
    snake_body.insert(0, pg.Rect(snake_body[-1].x, snake_body[-1].y, CELL_SIZE, CELL_SIZE))

    score_surface.fill((0, 0, 0))
    font_surface = font.render("Score: " + str(score), True, (255, 255, 255))

  # draw game
  draw_grid()
  for part in snake_body:
    pg.draw.rect(window, (255, 255, 255), part)

  pg.draw.rect(window, (255, 0, 0), apple)
  window.blit(score_surface, (0, 0))
  score_surface.blit(font_surface, (
    (score_surface.get_rect().width - font_surface.get_rect().width) / 2,
    (score_surface.get_rect().height - font_surface.get_rect().height) / 2
  ))

  pg.display.flip()
