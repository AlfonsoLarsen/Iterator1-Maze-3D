import numpy as np

# Define the maze
maze = np.random.randint(0, 2, size=(6, 6, 6))

print(maze)

# Define the start and end points
start = (0, 0, 0)
end = (5, 5, 5)

# Define the search function
def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y, z), path = stack.pop()

        if (x, y, z) not in visited:
            visited.add((x, y, z))

            if maze[x][y][z] == 1:
                continue

            if (x, y, z) == end:
                return path

            for dx, dy, dz in [(0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and 0 <= nz < maze.shape[2]:
                    stack.append(((nx, ny, nz), path + [(nx, ny, nz)]))

    return None

# Mark the start and end points in the maze
maze[start] = -1
maze[end] = -2

# Find a path through the maze
path = dfs(maze, start, end)

# Print the result
if path:
    print("Path found:", path)
else:
    print("No path found.")

