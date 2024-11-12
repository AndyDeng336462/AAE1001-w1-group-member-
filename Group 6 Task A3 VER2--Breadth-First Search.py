import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class BreadthFirstSearch:
    def __init__(self, ox, oy, grid_size, robot_radius):
        self.ox = ox
        self.oy = oy
        self.grid_size = grid_size
        self.robot_radius = robot_radius
        self.calc_obstacle_map()

    def calc_obstacle_map(self):
        self.min_x = round(min(self.ox))
        self.min_y = round(min(self.oy))
        self.max_x = round(max(self.ox))
        self.max_y = round(max(self.oy))

        self.x_width = round((self.max_x - self.min_x) / self.grid_size)
        self.y_width = round((self.max_y - self.min_y) / self.grid_size)

        self.obstacle_map = [[False for _ in range(self.y_width)] for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(self.ox, self.oy):
                    d = np.sqrt((iox - x)**2 + (ioy - y)**2)
                    if d <= self.robot_radius:
                        self.obstacle_map[ix][iy] = True
                        break

    def planning(self, sx, sy, gx, gy):
        start_node = (self.calc_xy_index(sx, self.min_x), self.calc_xy_index(sy, self.min_y))
        goal_node = (self.calc_xy_index(gx, self.min_x), self.calc_xy_index(gy, self.min_y))

        open_set = deque([start_node])
        closed_set = {}
        came_from = {}
        came_from[start_node] = None

        while open_set:
            current = open_set.popleft()
            
            if current == goal_node:
                return self.reconstruct_path(came_from, current)

            for move_x, move_y in self.get_motion_model():
                node = (current[0] + move_x, current[1] + move_y)
                if not self.verify_node(node):
                    continue
                if node in closed_set:
                    continue
                open_set.append(node)
                closed_set[node] = True
                came_from[node] = current

            # Update the plot less frequently to avoid crashes
            if len(closed_set) % 200 == 0:  # Update the plot every 200 iterations
                self.plot_current_path(closed_set, start_node, goal_node)

        return None

    def reconstruct_path(self, came_from, current):
        path = []
        while current:
            x = self.calc_grid_position(current[0], self.min_x)
            y = self.calc_grid_position(current[1], self.min_y)
            path.append((x, y))
            current = came_from[current]
        path.reverse()
        return path

    def calc_grid_position(self, index, min_pos):
        return index * self.grid_size + min_pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.grid_size)

    def verify_node(self, node):
        x, y = node
        if x < 0 or y < 0 or x >= self.x_width or y >= self.y_width:
            return False
        return not self.obstacle_map[x][y]

    def get_motion_model(self):
        motion = [[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1]]
        return motion

    def plot_current_path(self, closed_set, start, goal):
        plt.clf()
        for node in closed_set.keys():
            x = self.calc_grid_position(node[0], self.min_x)
            y = self.calc_grid_position(node[1], self.min_y)
            plt.plot(x, y, "xc")
        plt.plot(self.calc_grid_position(start[0], self.min_x), self.calc_grid_position(start[1], self.min_y), "og")
        plt.plot(self.calc_grid_position(goal[0], self.min_x), self.calc_grid_position(goal[1], self.min_y), "xb")
        for (ox, oy) in zip(self.ox, self.oy):
            plt.plot(ox, oy, "sk")
        plt.grid(True)
        plt.pause(0.001)

    def plot_final_path(self, path, start, goal):
        if path:
            plt.plot([x for x, y in path], [y for x, y in path], "-r")
        plt.plot(self.calc_grid_position(start[0], self.min_x), self.calc_grid_position(start[1], self.min_y), "og")
        plt.plot(self.calc_grid_position(goal[0], self.min_x), self.calc_grid_position(goal[1], self.min_y), "xb")
        for (ox, oy) in zip(self.ox, self.oy):
            plt.plot(ox, oy, "sk")
        plt.grid(True)
        plt.show()

def main():
    global start, goal, ox, oy
    start = (0, 0)
    goal = (50, 50)
    ox, oy = [], []

    for i in range(-10, 61): # draw the bottom border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 61): # draw the right border
        ox.append(61.0)
        oy.append(i)
    for i in range(-10, 0): # draw the top border
        ox.append(i)
        oy.append(61.0)
    for i in range(1, 62): # draw the top border
        ox.append(i)
        oy.append(61.0)
    for i in range(-10, 61): # draw the left border
        ox.append(-10.0)
        oy.append(i)
    for i in range(-10, 20): # draw the free border
        ox.append(10.0)
        oy.append(i)
    for i in range(0, 20): # draw the free border
        ox.append(i)
        oy.append(1.5 * i + 30)
    for j in range(10, 50): # draw the free border
        ox.append((j-170)/-4)
        oy.append(j)

    bfs = BreadthFirstSearch(ox, oy, grid_size=1, robot_radius=0.5)
    path = bfs.planning(start[0], start[1], goal[0], goal[1])

    # Plot final path
    bfs.plot_final_path(path, start, goal)

if __name__ == '__main__':
    main()
