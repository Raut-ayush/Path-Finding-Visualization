# pathfinding.py

from queue import PriorityQueue
from grid import EMPTY, WALL

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(grid, x, y):
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid.width and 0 <= ny < grid.height:
            if grid.grid[ny][nx] != WALL:
                yield (nx, ny)

def a_star_stepwise(grid):
    start = grid.start
    goal = grid.goal
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}

    visited = set()

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            # Yield final path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            yield {"path": path, "done": True}
            return

        visited.add(current)
        yield {"visited": set(visited), "path": []}

        for neighbor in neighbors(grid, *current):
            tentative = g_score[current] + 1
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                f_score = tentative + heuristic(neighbor, goal)
                open_set.put((f_score, neighbor))

    yield {"visited": set(visited), "path": [], "done": True}

def dijkstra_stepwise(grid):
    start = grid.start
    goal = grid.goal
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}

    visited = set()

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            yield {"path": path, "done": True}
            return

        visited.add(current)
        yield {"visited": set(visited), "path": []}

        for neighbor in neighbors(grid, *current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                open_set.put((new_cost, neighbor))

    yield {"visited": set(visited), "path": [], "done": True}
