# MapX – Warehouse Bot Simulator

MapX is a Python-based simulation tool for visualizing pathfinding algorithms like **A\*** and **Dijkstra** in a grid-based warehouse or factory setting. It allows you to place walls, set start/goal positions, and watch step-by-step how the bot finds its path in real time.

## 📦 Features

- Grid-based environment (customizable size)
- Wall placement with mouse
- Set Start and Goal positions
- Real-time visual comparison between:
  - A\* Algorithm (with Manhattan heuristic)
  - Dijkstra's Algorithm (uniform cost)
- Map save/load (`map.json`)
- Path and visited node visualization

---

## 🎮 Controls

| Action                  | Key/Mouse       |
|-------------------------|-----------------|
| Place/Remove Wall       | Left Click      |
| Set Start Position      | `S`             |
| Set Goal Position       | `G`             |
| Wall Drawing Mode       | `W`             |
| Select A* Algorithm     | `1`             |
| Select Dijkstra         | `2`             |
| Run Algorithm           | `SPACE`         |
| Save Map to `map.json`  | `K`             |
| Load Map from File      | `L`             |
| Quit                    | Close window    |

---

## 🧠 Algorithms

### A\*
- Uses Manhattan distance as a heuristic.
- Typically finds shorter paths faster.
- Favors paths closer to the goal.

### Dijkstra
- No heuristic.
- Explores all directions equally.
- Guaranteed shortest path but often slower.

---

## 📁 Project Structure
MapX/
│
├── main.py # App entry point
├── config.py # Grid and color settings
├── grid.py # Grid data logic
├── pathfinding.py # A*, Dijkstra stepwise logic
├── visualizer.py # Grid and path rendering (pygame)
├── map.json # Saved grid layout (walls/start/goal)
└── assets/ # (Optional: for future textures/sprites)

## 🚀 Requirements

- Python 3.8+
- [pygame](https://pypi.org/project/pygame/)

Install with:

```bash
pip install pygame
