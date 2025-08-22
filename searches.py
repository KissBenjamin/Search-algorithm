from algorithm_result import Result

def bfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        print(path)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def dfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        print(path)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.insert(0, new_path)

def check_if_goal_found_and_populate_neighbours(graph, key, neighbours, result):
    for node in graph.nodes[key]:
        result.extensions += 1
        if node == 'G':
            result.path += node
            return True
        neighbours.append(node)
    return False

def search_lowest_heuristic_value(graph, neighbours):
    min_number = 999999
    for node in neighbours:
        value = graph.heuristic_values[node]
        if value < min_number:
            min_number = value
            key = node
    return key

def hill_climing(graph):
    result = Result()
    result.path += 'S'
    key = 'S'
    is_goal_found = False
    neighbours = []

    while True:
        is_goal_found = check_if_goal_found_and_populate_neighbours(graph, key, neighbours, result)
        if is_goal_found:
            break
        key = search_lowest_heuristic_value(graph, neighbours)
        neighbours.remove(key)
        result.path += key
    return result

def best_first_search(graph):
    result = Result()
    queue = [{'node': 'S', 'path': ['S'], 'cost': 0, 'heuristic': graph.heuristic_values['S']}]
    visited = set()
    visited.add('S')
    goal = 'G'

    while queue:
        queue.sort(key=lambda x: x['heuristic'])
        current_node_info = queue.pop(0)
        node, path, cost = current_node_info['node'], current_node_info['path'], current_node_info['cost']

        if node == goal:
            result.path = ''.join(path)
            return result

        current_node = graph.nodes_with_weights[node]
        for item in current_node:
            result.extensions += 1
            for key, value in item.items():
                if key not in path and key not in visited:
                    visited.add(key)
                    new_path = path + [key]
                    new_cost = value + cost
                    heuristic_value = graph.heuristic_values.get(key, 0)
                    queue.append({'node': key, 'path': new_path, 'cost': new_cost, 'heuristic': heuristic_value})