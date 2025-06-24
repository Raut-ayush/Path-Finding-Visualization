# grid.py
from config import GRID_WIDTH, GRID_HEIGHT
import json
EMPTY = 0
WALL = 1
START = 2
GOAL = 3

class Grid:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]
        self.start = (0, 0)
        self.goal = (self.width - 1, self.height - 1)

    def toggle_wall(self, x, y):
        if self.grid[y][x] == WALL:
            self.grid[y][x] = EMPTY
        elif self.grid[y][x] == EMPTY:
            self.grid[y][x] = WALL

    def set_start(self, x, y):
        if self.start:
            sx, sy = self.start
            self.grid[sy][sx] = EMPTY
        self.start = (x, y)
        self.grid[y][x] = START

    def set_goal(self, x, y):
        if self.goal:
            gx, gy = self.goal
            self.grid[gy][gx] = EMPTY
        self.goal = (x, y)
        self.grid[y][x] = GOAL

    def save_to_file(self, filename="map.json"):
        data = {
            "grid": self.grid,
            "start": self.start,
            "goal": self.goal
        }
        with open(filename, "w") as f:
            json.dump(data, f)
        print(f"✅ Map saved to {filename}")

    def load_from_file(self, filename="map.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.grid = data["grid"]
                self.start = tuple(data["start"]) if data["start"] else None
                self.goal = tuple(data["goal"]) if data["goal"] else None
            print(f"📂 Map loaded from {filename}")
        except Exception as e:
            print(f"⚠️ Error loading map: {e}")