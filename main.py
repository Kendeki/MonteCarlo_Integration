import matplotlib.pyplot as plt
from numpy import linspace
from equation import Equation
from random import uniform

NUM_OF_POINTS = 500
positive_area = 0
negative_area = 0

eq = Equation(1, -5, 6)
a, b = 4, 6

x_values = linspace(a - 5, b + 5, 400)
y_values = eq.y_values(x_values)

ya_value = eq.solve(a)
yb_value = eq.solve(b)

rectangle_top = max(eq.y_values(linspace(a,b,400)))
rectangle_bottom = min(min(eq.y_values(linspace(a, b, 400))), 0)
rectangle_height = rectangle_top - rectangle_bottom
rectangle_base = b - a
rectangle_area = rectangle_base * rectangle_height

fig = plt.figure(figsize=(16, 9))
ax = fig.add_axes((0.05, 0.05, 0.95, 0.95))
plt.ion()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.grid(True)

ax.set_ylim(rectangle_bottom - 10, rectangle_top + 10)

ax.plot(x_values, y_values)
plt.pause(1)
ax.fill_between(linspace(a,b,400), eq.y_values(linspace(a,b,400)), color="#FF0000", alpha=0.15)
plt.pause(1)

ax.plot([a, b], [rectangle_top, rectangle_top], "#00FF00")
ax.plot([a, b], [rectangle_bottom, rectangle_bottom], "#00FF00")
ax.plot([a, a], [rectangle_bottom, rectangle_top], "#00FF00")
ax.plot([b, b], [rectangle_bottom, rectangle_top], "#00FF00")

ax.plot([a, a], [0, ya_value], "#FF0000")
ax.plot([b, b], [0, yb_value], "#FF0000")
plt.pause(1)

for _ in range(NUM_OF_POINTS):
    random_x = uniform(a, b)
    random_y = uniform(rectangle_bottom, rectangle_top)
    solution = eq.solve(random_x)
    inside_function = False

    if solution >= 0:
        if 0 <= random_y <= solution:
            positive_area += 1
            inside_function = True
    else:
        if solution <= random_y <= 0:
            negative_area += 1
            inside_function = True

    ax.plot(random_x, random_y, "go" if inside_function else "ro")
    plt.pause(0.001)

plt.ioff()

ax.text(0.5, 0.9, "\n".join([
    "Area = rectangle_area * ((positive_area - negative_area) / NUM_POINTS)",
    f"Area = {rectangle_area:.4f} * ({positive_area}/{NUM_OF_POINTS} - {negative_area}/{NUM_OF_POINTS})",
    f"Area = {rectangle_area:.4f} * ({positive_area/NUM_OF_POINTS:.4f} - {negative_area/NUM_OF_POINTS:.4f})",
    f"Area = {(rectangle_area * ((positive_area - negative_area) / NUM_OF_POINTS)):.4f}"
]), color='#000000', transform=ax.transAxes, bbox=dict(facecolor='none', edgecolor='red'))

plt.show()
