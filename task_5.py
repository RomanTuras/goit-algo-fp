import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    '''Node'''
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    '''Додавання зв'язків між вузлами дерева'''
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    '''Створює граф та визначає початкові позиції для вузлів дерева'''
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def increment_color(color):
    '''Логіка для зміни кольору'''
    r = min(int(color[1:3], 16) + 16, 255)
    g = min(int(color[3:5], 16) + 16, 255)
    b = min(int(color[5:7], 16) + 16, 255)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def bfs(node):
    '''Обхід бінарного дерева в ширину'''
    visited = []
    queue = [node]
    new_color=node.color
    while queue:
        current = queue.pop(0)
        if current:
            new_color = increment_color(new_color)
            current.color=new_color
            visited.append(current)
            queue.append(current.left)
            queue.append(current.right)
    return visited

stored_color = "#1296F0"

def dfs(node, visited=[]):
    '''Обхід бінарного дерева в глибину'''
    global stored_color
    if node is not None:
        stored_color = increment_color(stored_color)
        node.color = stored_color
        visited.append(node)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited


# Створення дерева
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(10)

# Візуалізація обходу бінарного дерева в ширину
bfs(root)
draw_tree(root)

# Візуалізація обходу бінарного дерева в глибину
dfs(root)
draw_tree(root)
