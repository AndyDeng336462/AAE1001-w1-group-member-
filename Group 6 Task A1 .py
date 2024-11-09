"""

A* grid planning

author: Atsushi Sakai(@Atsushi_twi)
        Nikos Kanargias (nkana@tee.gr)

See Wikipedia article (https://en.wikipedia.org/wiki/A*_search_algorithm)

This is the simple code for path planning class

"""

import math
import matplotlib.pyplot as plt

show_animation = True


class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """
        self.resolution = resolution
        self.rr = rr
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model()
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y

        self.Delta_C1 = 0.3
        self.Delta_C2 = 0.15
        self.costPerGrid = 1

    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x
            self.y = y
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return f"{self.x},{self.y},{self.cost},{self.parent_index}"

    def planning(self, sx, sy, cx1, cy1, cx2, cy2, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            c_x1: cp1 x position [m]
            c_y1: cp1 y position [m]
            c_x1: cp2 x position [m]
            c_y1: cp2 y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        checkpoint1_node = self.Node(self.calc_xy_index(cx1, self.min_x),
                                     self.calc_xy_index(cy1, self.min_y), 0.0, -1)
        checkpoint2_node = self.Node(self.calc_xy_index(cx2, self.min_x),
                                     self.calc_xy_index(cy2, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        checkpoints = [checkpoint1_node, checkpoint2_node, goal_node]
        open_set, closed_set = dict(), dict()
        open_sets = [dict() for _ in range(len(checkpoints) + 1)]
        open_sets[0][self.calc_grid_index(start_node)] = start_node
        open_set[self.calc_grid_index(start_node)] = start_node

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(checkpoints[0], open_set[o]))
            current = open_set[c_id]

            if current.x == checkpoints[0].x and current.y == checkpoints[0].y:
                if len(checkpoints) == 1:
                    print("Total Trip time required -> ", current.cost)
                    goal_node.parent_index = current.parent_index
                    goal_node.cost = current.cost
                    break
                else:
                    checkpoints.pop(0)
                    open_set.clear()
                    open_set[self.calc_grid_index(current)] = current

            if show_animation:
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            del open_set[c_id]
            closed_set[c_id] = current

            for i, _ in enumerate(self.motion):
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)

                if self.calc_grid_position(node.x, self.min_x) in self.tc_x and self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                    node.cost += self.Delta_C1 * self.motion[i][2]

                if self.calc_grid_position(node.x, self.min_x) in self.fc_x and self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                    node.cost += self.Delta_C2 * self.motion[i][2]

                n_id = self.calc_grid_index(node)

                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node
                else:
                    if open_set[n_id].cost > node.cost:
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(n1, n2):
        w = 1.0
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        return d

    def calc_grid_position(self, index, min_position):
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x or py < self.min_y or px >= self.max_x or py >= self.max_y:
            return False

        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):
        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)

        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True
                        break

    @staticmethod
    def get_motion_model():
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]]

        return motion


def main():
    print(__file__ + " start the A star algorithm demo !!")

    sx = 50.0
    sy = 30.0
    cx1 = 50.0
    cy1 = 5.0
    cx2 = 20.0
    cy2 = 30.0
    gx = 0.0
    gy = 60
    grid_size = 1
    robot_radius = 1.0

    ox, oy = [], []
    for i in range(-10, 61):
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 61):
        ox.append(61.0)
        oy.append(i)
    for i in range(-10, 0):
        ox.append(i)
        oy.append(61.0)
    for i in range(1, 62):
        ox.append(i)
        oy.append(61.0)
    for i in range(-10, 61):
        ox.append(-10.0)
        oy.append(i)
    for i in range(-10, 20):
        ox.append(10.0)
        oy.append(i)
    for i in range(0, 20):
        ox.append(i)
        oy.append(1.5 * i + 30)
    for j in range(10, 50):
        ox.append((j - 170) / -4)
        oy.append(j)

    tc_x, tc_y = [], []
    for i in range(20, 30):
        for j in range(0, 50):
            tc_x.append(i)
            tc_y.append(j)

    fc_x, fc_y = [], []
    for i in range(40, 60):
        for j in range(0, 10):
            fc_x.append(i)
            fc_y.append(j)

    if show_animation:
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "og")
        plt.plot(gx, gy, "xb")
        plt.plot(fc_x, fc_y, "oy")
        plt.plot(tc_x, tc_y, "or")
        plt.plot(cx1, cy1, "xb", markersize=2, markeredgewidth=2)
        plt.plot(cx2, cy2, "xb", markersize=2, markeredgewidth=2)
        plt.grid(True)
        plt.axis("equal")

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, cx1, cy1, cx2, cy2, gx, gy)

    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.pause(0.001)
        plt.show()


if __name__ == '__main__':
    main()

