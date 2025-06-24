# main.py

import pygame
from config import *
from grid import Grid
from visualizer import draw_grid, draw_path
from pathfinding import a_star_stepwise, dijkstra_stepwise

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MapX – Warehouse Bot Simulator")
clock = pygame.time.Clock()

grid = Grid()
path = []
visited = set()
step_generator = None
algorithm = "astar"  # default
mode = 'wall'
running = True

print("Instructions:")
print("Left Click: Place walls")
print("Press S: Set Start | G: Set Goal | W: Wall mode")
print("Press 1: A* | 2: Dijkstra | SPACE: Run algorithm")
print("Press K: Save | L: Load")

while running:
    screen.fill(WHITE)

    # 🧭 Draw visited nodes (optional light blue)
    draw_grid(screen, grid, visited)

    # 🟣 Draw final path
    draw_path(screen, path)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                mode = 'start'
                print("Mode: Set Start")
            elif event.key == pygame.K_g:
                mode = 'goal'
                print("Mode: Set Goal")
            elif event.key == pygame.K_w:
                mode = 'wall'
                print("Mode: Place Walls")
            elif event.key == pygame.K_1:
                algorithm = "astar"
                print("🔁 Selected Algorithm: A*")
            elif event.key == pygame.K_2:
                algorithm = "dijkstra"
                print("🔁 Selected Algorithm: Dijkstra")
            elif event.key == pygame.K_k:
                grid.save_to_file("map.json")
            elif event.key == pygame.K_l:
                grid.load_from_file("map.json")
            elif event.key == pygame.K_SPACE:
                visited = set()
                path = []
                if algorithm == "astar":
                    step_generator = a_star_stepwise(grid)
                else:
                    step_generator = dijkstra_stepwise(grid)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            gx, gy = mx // CELL_SIZE, my // CELL_SIZE
            if mode == 'wall':
                grid.toggle_wall(gx, gy)
            elif mode == 'start':
                grid.set_start(gx, gy)
            elif mode == 'goal':
                grid.set_goal(gx, gy)

    # 🔄 Animate algorithm step-by-step
    if step_generator:
        try:
            step = next(step_generator)
            visited = step.get("visited", visited)
            path = step.get("path", path)
            if step.get("done"):
                print(f"✅ Path found: {len(path)} steps" if path else "❌ No path.")
                step_generator = None
        except StopIteration:
            step_generator = None

    clock.tick(20)  # Lower FPS for visible animation

pygame.quit()
