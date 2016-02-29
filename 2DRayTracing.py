import matplotlib.pyplot as plt
import matplotlib.patches as patches

res_x = 1
res_y = 1

p0 = (0, 0)  # (x, y)
p1 = (15, 18)

dx = (p1[0] - p0[0]) / res_x
dy = (p1[1] - p0[1]) / res_y

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

err_x = dx
err_y = dy

x = p0[0]
y = p0[1]

visited_cells = []

while x != p1[0] or y != p1[1]:
    visited_cells.append((x, y))

    if err_x > err_y:
        x += sx
        err_y += dy
    elif err_y > err_x:
        y += sy
        err_x += dx
    else:
        x += sx
        y += sy
        err_x += dx
        err_y += dy

fig = plt.figure()

ax = fig.add_subplot(111, aspect='equal')

for cell in visited_cells:
    ax.add_patch(
        patches.Rectangle(
            (cell[0], cell[1]),  # (x,y)
            res_x,  # width
            res_y,  # height
        )
    )

ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color='red')

plt.show()
