import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from collections import deque
import numpy as np

# 定義網格大小
grid_size = (100, 100)

# 手動設置障礙物以形成曲折的路徑
obstacles = set()

# 添加一些直線障礙物
for i in range(15, 80):
    obstacles.add((i, 50))
    obstacles.add((50, i))

# 添加一些曲折的障礙物
for i in range(10, 45):
    obstacles.add((i, i + 20))
    obstacles.add((i + 20, i))

for i in range(65, 90):
    obstacles.add((i, 90 - i))
    obstacles.add((90 - i, i))

# 確保起點和終點不在障礙物中
obstacles.discard((0, 0))
obstacles.discard((grid_size[0] - 1, grid_size[1] - 1))

# 定義起點和終點
start = (0, 0)
goal = (grid_size[0] - 1, grid_size[1] - 1)

# 初始化網格
grid = np.zeros(grid_size)
for obs in obstacles:
    grid[obs] = -1  # 障礙物標記為-1

# BFS搜索
def bfs(start, goal, grid):
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    # 定義八個方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size[0] and 0 <= ny < grid_size[1]:
                if (nx, ny) not in visited and grid[nx, ny] != -1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current

    # 回溯路徑
    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()
    return path

# 獲取搜索路徑
path = bfs(start, goal, grid)

# 動畫展示
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-1, grid_size[1] + 1)
ax.set_ylim(-1, grid_size[0] + 1)
ax.set_xticks(np.arange(-1, grid_size[1] + 1, 10))
ax.set_yticks(np.arange(-1, grid_size[0] + 1, 10))
ax.grid(True)

# 繪製障礙物
for obs in obstacles:
    ax.add_patch(patches.Rectangle((obs[1], grid_size[0] - obs[0] - 1), 1, 1, color='black'))

# 繪製起點和終點
ax.add_patch(patches.Rectangle((start[1], grid_size[0] - start[0] - 1), 1, 1, color='green'))
ax.add_patch(patches.Rectangle((goal[1], grid_size[0] - goal[0] - 1), 1, 1, color='red'))

# 初始化搜索過程
search_path = []

def update(frame):
    if frame < len(path):
        step = path[frame]
        search_path.append(step)
        ax.add_patch(patches.Rectangle((step[1], grid_size[0] - step[0] - 1), 1, 1, color='blue', alpha=0.5))

ani = FuncAnimation(fig, update, frames=len(path), repeat=False, interval=10)
plt.show()