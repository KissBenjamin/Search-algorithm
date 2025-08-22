from graph import Graph

def is_next_graph(current_line):
    if current_line.startswith('graph'):
        return True
    else:
        return False

def read_graphs():
    raw_graphs = [[]]
    with open('data/graphs.txt') as f:
        lines = f.read().splitlines()
        current_graph_id = 0
        for i in range(1, len(lines)):
            current_line = lines[i]
            if (is_next_graph(current_line)):
                current_graph_id += 1
                raw_graphs.append([])
            else:
                raw_graphs[current_graph_id].append(current_line.upper())
    return raw_graphs


def build_nodes(raw_graph):
    nodes = {}
    node_names = set(raw_graph[0].split(' '))
    for name in node_names:
        nodes.update({name: []})

    for i in range(2, len(raw_graph)):
        line = raw_graph[i]

        splitted_line = line.split(' ')
        nodes[splitted_line[0]].append(splitted_line[1])
    return nodes

def build_nodes_with_weights(raw_graph):
    nodes = {}
    node_names = set(raw_graph[0].split(' '))
    for name in node_names:
        nodes.update({name: []})

    for i in range(2, len(raw_graph)):
        line = raw_graph[i]

        splitted_line = line.split(' ')
        nodes[splitted_line[0]].append({splitted_line[1]: int(splitted_line[2])})
    return nodes


def build_heuristic_values(raw_graph):
    keyvalues = raw_graph[1][2:].split(' ')
    heuristic_values = {}
    for item in keyvalues:
        heuristic_values.update({item.split('-')[0]: int(item.split('-')[1])})
    return heuristic_values

def build_graph(raw_graph):
    nodes = build_nodes(raw_graph)
    nodes_with_weights = build_nodes_with_weights(raw_graph)
    heuristic_values = build_heuristic_values(raw_graph)
    return Graph(nodes, nodes_with_weights, heuristic_values)

def build_graphs():
    raw_graphs = read_graphs()
    graphs = []
    for item in raw_graphs:
        graphs.append(build_graph(item))
    return graphs