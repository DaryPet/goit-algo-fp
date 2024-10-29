import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import colorsys

# class for node
class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# adding nodes and edges to graph
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer= layer + 1 )

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y= y - 1, layer=layer + 1)

    return graph

# tree visualisation
def draw_tree(tree_root, visited_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0,0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_nodes.get(node[0], "#000000") for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8,5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# add function DFS
def dfs_traversal(root):
    stack = [root]
    visited_nodes = {}
    steps = 0
    total_nodes = count_nodes(root)

    while stack:
        current =  stack.pop()
        if current:
            # color depends on order
            color = generate_color(steps, total_nodes)
            visited_nodes[current.id] = color
            steps += 1

            # visualisation for each step
            draw_tree(root, visited_nodes)

            # add nodes to right, left
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

# function for BFS
def bfs_traversal(root):
    queue = deque([root])
    visited_nodes = {}
    steps = 0
    total_nodes = count_nodes(root)

    while queue:
        current = queue.popleft()
        if current:
            # add color depending on order
            color =  generate_color(steps, total_nodes)
            visited_nodes[current.id] = color
            steps += 1

            # visualisation for each step
            draw_tree(root, visited_nodes)

            # add left node first, then right node
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

# color generation
def generate_color(step, total_steps):
    hue = 0.6
    saturation = 1.0
    value = (step + 1) / total_steps
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

# add nodes counting
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)



# implementing
if __name__ == "__main__":
    # creating tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
   
#    DFS
    print("DFS:")
    dfs_traversal(root)

    # BFS
    print("BFS:")
    bfs_traversal(root)