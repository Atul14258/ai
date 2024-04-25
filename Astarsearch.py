def a_star_algo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    def get_neighbors(v):
        if v in graph_nodes:
            return graph_nodes[v]
        else:
            return None

    def heuristic(n):
        h_dist = {
            'S': 5,
            'A': 3,
            'B': 4,
            'C': 2,
            'D': 6,
            'G': 0
        }
        return h_dist[n]

    while open_set:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or n not in graph_nodes:
            break

        open_set.remove(n)
        closed_set.add(n)

        for m, weight in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)

    if stop_node not in parents or stop_node not in graph_nodes:
        print("Path does not exist!")
        return None

    path = [stop_node]
    fitness_numbers = [g[stop_node] + heuristic(stop_node)]
    while parents[path[-1]] != path[-1]:
        path.append(parents[path[-1]])
        fitness_numbers.append(g[path[-1]] + heuristic(path[-1]))
    path.reverse()
    fitness_numbers.reverse()

    print("Start node:", start_node)
    print("Goal node:", stop_node)
    print("Weight of the path:", g[stop_node])
    print("Path found:")
    for i in range(len(path)):
        print("Node:", path[i], ", Fitness Number:", fitness_numbers[i])
    return path

# Define your graph here
graph_nodes = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 15)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

start_node = input("Enter the start node: ")
stop_node = input("Enter the goal node: ")

path = a_star_algo(start_node, stop_node)
if path:
    print("Path:", path)

# Start Node - S, Goal Node - G