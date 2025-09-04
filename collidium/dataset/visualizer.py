import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def visualize_circle_collision(row):
	# row: structured numpy array or dict with keys x1, y1, x2, y2, r1, r2, p1x, p1y, p2x, p2y, flag
	fig, ax = plt.subplots()
	# Draw circles
	circle1 = Circle((row['x1'], row['y1']), row['r1'], fill=False, edgecolor='blue', linewidth=2)
	circle2 = Circle((row['x2'], row['y2']), row['r2'], fill=False, edgecolor='green', linewidth=2)
	ax.add_patch(circle1)
	ax.add_patch(circle2)
	# Draw collision/shortest line
	color = 'red' if row['flag'] else 'black'
	ax.plot([row['p1x'], row['p2x']], [row['p1y'], row['p2y']], color=color, linewidth=2)
	# Mark points
	ax.scatter([row['p1x'], row['p2x']], [row['p1y'], row['p2y']], color=color)
	# Set limits
	ax.set_aspect('equal')
	ax.set_xlim(min(row['x1']-row['r1'], row['x2']-row['r2'])-1, max(row['x1']+row['r1'], row['x2']+row['r2'])+1)
	ax.set_ylim(min(row['y1']-row['r1'], row['y2']-row['r2'])-1, max(row['y1']+row['r1'], row['y2']+row['r2'])+1)
	plt.show()
