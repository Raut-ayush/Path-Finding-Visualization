# visualizer.py
import pygame
from config import *
from grid import EMPTY, WALL, START, GOAL

def draw_grid(screen, grid_obj, visited=None):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            val = grid_obj.grid[y][x]

            if visited and (x, y) in visited:
                color = (173, 216, 230)  # Light blue for visited
            elif val == EMPTY:
                color = WHITE
            elif val == WALL:
                color = BLACK
            elif val == START:
                color = GREEN
            elif val == GOAL:
                color = RED
            else:
                color = GRAY

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_path(screen, path):
    from config import CELL_SIZE, BLUE
    for x, y in path:
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        surface.fill((*BLUE, 255))
        screen.blit(surface, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)
