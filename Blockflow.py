import matplotlib.pyplot as plt
import networkx as nx
import random
from pprint import pprint
from itertools import groupby
from queue import Queue


def read_dataset(path, delimiter=" "):
    # Reading given dataset for drawing graph
    g = nx.read_edgelist(path, create_using=nx.Graph(), nodetype=int, delimiter=delimiter)
    return g


def UndirectedCycles(G, root=None):  # because the graph is undirected the cycles will be undirected
    gnodes = set(G.nodes())  # creating set of nodes
    cycles = []  # creating a list for cycles
    while gnodes:  # loop over connected components
        if root is None:
            root = gnodes.pop()
        stack = [root]
        pred = {root: root}
        used = {root: set()}
        while stack:  # finding cycles
            z = stack.pop()  # use last-in so cycles easier to find
            zused = used[z]
            for nbr in G[z]:
                if nbr not in used:  # new node
                    pred[nbr] = z
                    stack.append(nbr)
                    used[nbr] = {z}
                elif nbr == z:  # self loops
                    cycles.append([z])
                elif nbr not in zused:  # found a cycle
                    pn = used[nbr]
                    cycle = [nbr, z]
                    p = pred[z]
                    while p not in pn:
                        cycle.append(p)
                        p = pred[p]
                    cycle.append(p)
                    cycles.append(cycle)
                    used[nbr].add(z)
        gnodes -= set(pred)
        root = None
    return cycles


def BFS(edge_list, start_node, target_node):
    # Set of visited nodes to prevent loops
    visited = set()
    queue = Queue()

    # Add the start_node to the queue and visited list
    queue.put(start_node)
    visited.add(start_node)

    # start_node has not parents
    parent = dict()
    parent[start_node] = None

    # Performing some conditionds for finding the path
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for next_node in edge_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    # Path reconstruction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node])
            target_node = parent[target_node]
        path.reverse()
    return path


def find_diameters(g):
    nodes = list(g.nodes)
    all_paths = []
    node_size = len(nodes)
    for i in range(node_size):
        for j in range(i + 1, node_size):
            paths = list(BFS(g, nodes[i], nodes[j]))
            all_paths.append(paths)
    return all_paths


def adj_list(g):
    edges = list(g.edges)
    l2 = [t[::-1] for t in edges]
    resultList = list(set(edges) | set(l2))

    adj = {k: [v[1] for v in g] for k, g in groupby(sorted(resultList), lambda e: e[0])}
    return adj
    # adj: {1: [2, 3], 2: [3]}

def dfs(adj_list, start, target, path, visited=None):
    if not visited:
        visited = set()
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    adj_of_start = {node: adj_list[node] for node in adj_list[start]}
    sorted_by_most_common_adjs = list(sorted(
        adj_of_start.items(),
        key=lambda item: len(set(item[1]) & set(adj_list[start])),
        reverse=True))
    for neighbour, _ in sorted_by_most_common_adjs:

        if neighbour not in visited:
            result = dfs(adj_list, neighbour, target, path, visited)
            if result is not None:
                return result


def random_dfs(g, a, b):
    nodes = list(g.nodes)
    traversal_path = dfs(adj_list(g), a, b, [])
    while traversal_path is None:
        n1 = random.choice(nodes)
        n2 = random.choice(nodes)
        print(f"No path found\nstart node: {n1}, target node: {n2}")
        traversal_path = dfs(adj_list(g), n1, n2, [])
    return traversal_path


def main():
    #first part
    g = read_dataset("blockflow.txt", " ")  #for blockflow_2.text delimiter is ","
    print("All Cycles of this Network are = ", UndirectedCycles(g))
    cycles = UndirectedCycles(g)
    print("Number of Cycles in this Network is = ", len(cycles))
    Transactions = [cycle for cycle in cycles if len(cycle) == 5]
    print("Transactions can be Authenticated = ", Transactions)
    print("Number of Transactions can be Authenticated =", len(Transactions))
    print(nx.info(g))
    #nx.draw(g, with_labels=True, node_size=200, node_color='red')
    #plt.show() #for running the code faster make it a comment

    #use this code just for blockflow_2.txt dataset for second part of homework,otherwise make it comment
    '''all_paths = find_diameters(g)
    max_path = max(all_paths, key=len)
    max_paths = [path for path in all_paths if len(path) == len(max_path)]
    paths = [{"from Node": path[0], "to Node": path[-1], "path": path} for path in max_paths]
    print(paths)
    print("The Diameter of Network is =", len(max_path) - 1)
    print("Number of pair nodes that their distance is equal to Diameter =", len(max_paths))'''

    #third part
    print(adj_list(g)) #for running the code faster make it a comment
    a, b = input("Enter nodes: ").split(" ")
    a, b = int(a), int(b)
    traversal_path = random_dfs(g, a, b)
    print(traversal_path)


if __name__ == '__main__':
    main()
