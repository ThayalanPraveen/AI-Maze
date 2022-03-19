import queue
from queue import PriorityQueue
import random

# start node is set as 1
# end node is set as 3
# barriers are set as 2
total_cost = 0
found = False
out = True
bfs_loop_count = 0
dfs_loop_count = 0
ucs_loop_count = 0
befs_loop_count = 0
as_loop_count = 0
e_node = 0
s_node = 0
b_node = []
node_list = [0]
M = [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]


def fill_maze(M, size):
    count = 0
    count2 = 0
    for i in M:
        count = 0
        count = count + count2
        count2 = count2 + 1

        for j in range(0, size):
            i[j] = count
            count = count + size


def generate_node(maze, start, end, node_val):
    global s_node
    global e_node
    global b_node
    node = random.randint(start, end)  # Generating a start node between start & end
    node_response = False
    while not node_response:  # Repeat node generation until a non repeating node is created
        node = random.randint(start, end)
        node_response = node_check(node)
    if node_val == "Start":
        s_node = node
    if node_val == "End":
        e_node = node
    if node_val == "Barrier":
        b_node.append(node)
    node_list.append(node)  # Add generated node to a list to check later
    maze[node % 8][node // 8] = node_val  # Passing the row and column in the maze to set the start node


def node_check(node):
    global found
    for x in node_list:
        if x == node:
            found = True
    if found:
        found = False
        return False  # if node is found in the node_list array this will return false
    else:
        return True  # if node is found in the node_list array this will return true


# BFS
def bfs(s):
    print("BFS Search ----")
    global bfs_loop_count
    bfs_loop_count = 0
    # Mark all the vertices as not visited
    visited = [False] * 64

    # Create a queue for BFS
    queue = []

    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:
        bfs_loop_count = bfs_loop_count + 1
        # Dequeue value from
        # queue and print it
        s = queue.pop(0)
        print(s, end=" ")
        if s == "End":
            print("\nNumber of Nodes visited for BFS: ", bfs_loop_count)
            break
        # Get all adjacent values of s
        # has not been visited, then mark it
        # visited and enqueue it
        row = s % 8
        column = s // 8
        i_left = column - 1
        i_top = row - 1
        i_bottom = row + 1
        i_right = column + 1
        if i_left >= 0 and M[row][i_left] != "Barrier":
            if not visited[s - 8]:
                queue.append(M[row][i_left])
                visited[s - 8] = True
        if i_top >= 0 and M[i_top][column] != "Barrier":
            if not visited[s - 1]:
                queue.append(M[i_top][column])
                visited[s - 1] = True
        if i_bottom <= 7 and M[i_bottom][column] != "Barrier":
            if not visited[s + 1]:
                queue.append(M[i_bottom][column])
                visited[s + 1] = True
        if i_right <= 7 and M[row][i_right] != "Barrier":
            if not visited[s + 8]:
                queue.append(M[row][i_right])
                visited[s + 8] = True


def DFSUtil(s, visited1):
    global out
    global dfs_loop_count
    dfs_loop_count = dfs_loop_count + 1
    # Mark the current node as visited
    # and print it
    visited1.append(s)
    if s == e_node:
        print("End", end=' ')
        print("\nNumber of Nodes visited for DFS: ", dfs_loop_count)
        out = False
    if out:
        print(s, end=' ')
    # Recur for all the vertices
    # adjacent to this vertex
    row = s % 8
    column = s // 8
    i_left = column - 1
    i_top = row - 1
    i_bottom = row + 1
    i_right = column + 1
    if i_left >= 0 and M[row][i_left] != "Barrier":
        if not visited1[s - 8]:
            visited1[s - 8] = True
            DFSUtil(s - 8, visited1)
    if i_top >= 0 and M[i_top][column] != "Barrier":
        if not visited1[s - 1]:
            visited1[s - 1] = True
            DFSUtil(s - 1, visited1)
    if i_bottom <= 7 and M[i_bottom][column] != "Barrier":
        if not visited1[s + 1]:
            visited1[s + 1] = True
            DFSUtil(s + 1, visited1)
    if i_right <= 7 and M[row][i_right] != "Barrier":
        if not visited1[s + 8]:
            visited1[s + 8] = True
            DFSUtil(s + 8, visited1)


def DFS(v):
    print("\nDFS Search ----")
    # Create a set to store visited vertices
    visited = [False] * 64

    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(v, visited)


def heuristic_cost(n, g):
    nx = n // 8
    ny = n % 8
    gx = g // 8
    gy = g % 8
    cost = abs(nx - gx) + abs(ny - gy)
    return cost


def ucs(s, goal):
    global ucs_loop_count
    print("UCS Search")
    global total_cost
    visited = [False] * 64
    queue = PriorityQueue()
    queue.put((0, s))

    while queue:
        ucs_loop_count = ucs_loop_count + 1
        cost, node = queue.get()
        print(node, end=" ")
        if node == goal:
            print("\nNumber of Nodes visited for UCS: ", ucs_loop_count)
            print("Total cost is : ", total_cost)
            return total_cost
        row = node % 8
        column = node // 8
        i_left = column - 1
        i_top = row - 1
        i_bottom = row + 1
        i_right = column + 1
        if i_left >= 0 and M[row][i_left] != "Barrier":
            if not visited[node - 8]:
                total_cost = cost + 1
                queue.put((total_cost, node - 8))
                visited[node - 8] = True
        if i_top >= 0 and M[i_top][column] != "Barrier":
            if not visited[node - 1]:
                total_cost = cost + 1
                queue.put((total_cost, node - 1))
                visited[node - 1] = True
        if i_bottom <= 7 and M[i_bottom][column] != "Barrier":
            if not visited[node + 1]:
                total_cost = cost + 1
                queue.put((total_cost, node + 1))
                visited[node + 1] = True
        if i_right <= 7 and M[row][i_right] != "Barrier":
            if not visited[node + 8]:
                total_cost = cost + 1
                queue.put((total_cost, node + 8))
                visited[node + 8] = True


def befs(s, goal):
    global befs_loop_count
    print("Best First Search")
    global total_cost
    visited = [False] * 64
    queue = PriorityQueue()
    queue.put((0, s))

    while queue:
        befs_loop_count = befs_loop_count + 1
        cost, node = queue.get()
        print(node, end=" ")
        if node == goal:
            print("\nNumber of Nodes visited for UCS: ", ucs_loop_count)
            return total_cost
        row = node % 8
        column = node // 8
        i_left = column - 1
        i_top = row - 1
        i_bottom = row + 1
        i_right = column + 1
        if i_left >= 0 and M[row][i_left] != "Barrier":
            if not visited[node - 8]:
                cost2 = heuristic_cost(node-8,e_node)
                queue.put((cost2, node - 8))
                visited[node - 8] = True
        if i_top >= 0 and M[i_top][column] != "Barrier":
            if not visited[node - 1]:
                cost2 = heuristic_cost(node - 1, e_node)
                queue.put((cost2, node - 1))
                visited[node - 1] = True
        if i_bottom <= 7 and M[i_bottom][column] != "Barrier":
            if not visited[node + 1]:
                cost2 = heuristic_cost(node +1 , e_node)
                queue.put((cost2, node + 1))
                visited[node + 1] = True
        if i_right <= 7 and M[row][i_right] != "Barrier":
            if not visited[node + 8]:
                cost2 = heuristic_cost(node + 8, e_node)
                queue.put((cost2, node + 8))
                visited[node + 8] = True


def A_star(s, goal):
    global as_loop_count
    print("A* Search")
    global total_cost
    visited = [False] * 64
    queue = PriorityQueue()
    queue.put((0, s))

    while queue:
        as_loop_count = as_loop_count + 1
        cost, node = queue.get()
        print(node, end=" ")
        if node == goal:
            print("\nNumber of Nodes visited for UCS: ", ucs_loop_count)
            return total_cost
        row = node % 8
        column = node // 8
        i_left = column - 1
        i_top = row - 1
        i_bottom = row + 1
        i_right = column + 1
        if i_left >= 0 and M[row][i_left] != "Barrier":
            if not visited[node - 8]:
                cost2 = heuristic_cost(node-8,e_node) + heuristic_cost(node - 8, s_node) + 1
                queue.put((cost2, node - 8))
                visited[node - 8] = True
        if i_top >= 0 and M[i_top][column] != "Barrier":
            if not visited[node - 1]:
                cost2 = heuristic_cost(node - 1, e_node)+ heuristic_cost(node -1, s_node) + 1
                queue.put((cost2, node - 1))
                visited[node - 1] = True
        if i_bottom <= 7 and M[i_bottom][column] != "Barrier":
            if not visited[node + 1]:
                cost2 = heuristic_cost(node +1 , e_node) + heuristic_cost(node + 1, s_node) + 1
                queue.put((cost2, node + 1))
                visited[node + 1] = True
        if i_right <= 7 and M[row][i_right] != "Barrier":
            if not visited[node + 8]:
                cost2 = heuristic_cost(node + 8, e_node) + heuristic_cost(node + 8, s_node) + 1
                queue.put((cost2, node + 8))
                visited[node + 8] = True


def make_maze():
    # Fill the maze with
    fill_maze(M, 8)

    # Generating the starting node
    generate_node(M, 0, 15, "Start")
    print("Start node : ", s_node)

    # Generating the Goal node
    generate_node(M, 48, 63, "End")
    print("End node : ", e_node)

    print("Barrier Nodes: ", end=" ")
    # Generating the barriers
    for y in range(6):
        generate_node(M, 0, 63, "Barrier")
        print(b_node[y], end=" ")
    print()


make_maze()
print("\n******")
bfs(s_node)  # Run BFS from the start node
print("\n******")
DFS(s_node)  # Run DFS from the start node
print("\n******")
ucs(s_node, e_node)  # Run ucs from the start node
print("\n******")
befs(s_node, e_node)  # Run ucs from the start node
print("\n******")
A_star(s_node, e_node)  # Run ucs from the start node
print("\n******")