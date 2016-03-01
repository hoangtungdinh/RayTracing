from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def main():
    res_x = 1
    res_y = 1
    res_z = 1

    p0 = (4, 3, 2)  # (x, y, z)
    p1 = (10, 11, 12)

    dx = (p1[0] - p0[0]) / res_x
    dy = (p1[1] - p0[1]) / res_y
    dz = (p1[2] - p0[2]) / res_z

    if dx < 0:
        dx = -dx
        sx = -res_x
    else:
        sx = res_x

    if dy < 0:
        dy = -dy
        sy = -res_y
    else:
        sy = res_y

    if dz < 0:
        dz = -dz
        sz = -res_z
    else:
        sz = res_z

    step_x = (sx - res_x) / 2
    step_y = (sy - res_y) / 2
    step_z = (sz - res_z) / 2

    if dx == 0:
        dx = 1
        sx = 0
    if dy == 0:
        dy = 1
        sy = 0
    if dz == 0:
        dz = 1
        sz = 0

    err_x = dx * dy + dx * dz
    err_y = dy * dx + dy * dz
    err_z = dz * dx + dz * dy

    x = p0[0]
    y = p0[1]
    z = p0[2]

    visited_cells = []

    while x != p1[0] or y != p1[1] or z != p1[2]:
        visited_cells.append((x + step_x, y + step_y, z + step_z))

        if err_x > err_y and err_x > err_z:
            x += sx
            err_y += dy * dz
            err_z += dz * dy
        elif err_y > err_x and err_y > err_z:
            y += sy
            err_x += dx * dz
            err_z += dz * dx
        elif err_z > err_x and err_z > err_y:
            z += sz
            err_x += dx * dy
            err_y += dy * dx
        elif err_x == err_y and err_x > err_z:
            x += sx
            err_y += dy * dz
            err_z += dz * dy

            y += sy
            err_x += dx * dz
            err_z += dz * dx
        elif err_y == err_z and err_y > err_x:
            y += sy
            err_x += dx * dz
            err_z += dz * dx

            z += sz
            err_x += dx * dy
            err_y += dy * dx
        elif err_x == err_z and err_x > err_y:
            x += sx
            err_y += dy * dz
            err_z += dz * dy

            z += sz
            err_x += dx * dy
            err_y += dy * dx
        else:
            x += sx
            err_y += dy * dz
            err_z += dz * dy

            y += sy
            err_x += dx * dz
            err_z += dz * dx

            z += sz
            err_x += dx * dy
            err_y += dy * dx

    print(visited_cells)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect("equal")

    for cell in visited_cells:
        draw_cube(ax, cell, res_x, res_y, res_z)

    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], [p0[2], p1[2]], color='red')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    s_min = min(min(p0), min(p1))
    s_max = max(max(p0), max(p1))
    ax.auto_scale_xyz([s_min, s_max], [s_min, s_max], [s_min, s_max])
    ax.xaxis.set_ticks(range(s_min, s_max + res_x, res_x))
    ax.yaxis.set_ticks(range(s_min, s_max + res_y, res_y))
    ax.zaxis.set_ticks(range(s_min, s_max + res_z, res_z))

    plt.show()


def draw_cube(ax, cell, res_x, res_y, res_z):
    X, Y = np.meshgrid([cell[0], cell[0] + res_x], [cell[1], cell[1] + res_x])
    ax.plot_surface(X, Y, cell[2], alpha=0.2)
    ax.plot_surface(X, Y, cell[2] + res_z, alpha=0.2)

    Y, Z = np.meshgrid([cell[1], cell[1] + res_y], [cell[2], cell[2] + res_z])
    ax.plot_surface(cell[0], Y, Z, alpha=0.2)
    ax.plot_surface(cell[0] + res_x, Y, Z, alpha=0.2)

    X, Z = np.meshgrid([cell[0], cell[0] + res_x], [cell[2], cell[2] + res_z])
    ax.plot_surface(X, cell[1], Z, alpha=0.2)
    ax.plot_surface(X, cell[1] + res_y, Z, alpha=0.2)

if __name__ == "__main__":
    main()
