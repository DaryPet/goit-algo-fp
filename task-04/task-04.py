import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# class for node
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# making bynary tree from heap
def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None
    
    # making Node with values from heap
    node = Node(heap[index])
    # recursion, making left and right nodes
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)

    return node

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
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0,0)}
    tree = add_edges(tree, tree_root, pos)

    color = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8,5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=color)
    plt.show()

# implementing
if __name__ == "__main__":
    # creating heap
    heap=[10,5,3,2,4,1]
    heapq.heapify(heap)

    # creating tree from heap
    root = heap_to_tree(heap)

    # tree visualisation
    if root:
        draw_tree(root)