# 🧭 MapX – Pathfinding & Simulation Visualizer

MapX is an interactive Python-based simulator for visualizing and comparing popular pathfinding algorithms like **A\*** and **Dijkstra's Algorithm** on a 2D grid. Designed for educational and research purposes, it also emulates real-world warehouse or robotic bot navigation.

---

## 🧠 Key Features

- 🔁 **Real-time visualization** of pathfinding (step-by-step animation)
- ✅ Supports **A\*** (with heuristic) and **Dijkstra's** (uniform cost)
- 🧱 Click-to-place **walls**, **start**, and **goal** nodes
- 💾 Save and load maps (`map.json`)
- 🎯 Algorithm switching at runtime
- 🧩 Modular, readable Python code using **pygame**

---

## 🕹️ Controls

| Key / Mouse | Action                         |
|-------------|--------------------------------|
| Left Click  | Place/Remove Wall              |
| `S`         | Set Start Position             |
| `G`         | Set Goal Position              |
| `W`         | Switch to Wall Drawing Mode    |
| `1`         | Select A\* Algorithm            |
| `2`         | Select Dijkstra's Algorithm     |
| `SPACE`     | Run Selected Pathfinding Algo  |
| `K`         | Save Map to `map.json`         |
| `L`         | Load Map from `map.json`       |
| `X` / `ESC` | Exit / Close Window            |

---

## 📦 Project Structure

MapX/
├── main.py # Entry point – handles UI and control flow
├── config.py # Constants for grid size and colors
├── grid.py # Grid data model: walls, start, goal
├── pathfinding.py # Algorithms: A*, Dijkstra (stepwise generators)
├── visualizer.py # Grid + path + visited rendering (pygame)
├── map.json # Sample saved map (walls/start/goal)


## 🔍 Algorithms Compared

| Algorithm | Heuristic | Optimal Path | Speed      |
|-----------|-----------|--------------|------------|
| A\*       | ✅ Yes     | ✅ Yes        | ⚡ Faster   |
| Dijkstra  | ❌ No      | ✅ Yes        | 🐢 Slower   |

- **A\*** uses *Manhattan distance* to prioritize nodes closer to the goal.
- **Dijkstra** explores all equally, good for uniform-cost terrain.

---

## 🚀 Getting Started

### 📦 Install Requirements

```bash
pip install pygame
