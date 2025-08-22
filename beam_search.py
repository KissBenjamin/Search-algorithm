import functools
from algorithm_result import Result

class BeamSearch:
    def __init__(self, nodes_with_weights, heuristic_values):
        self.nodes_with_weights = nodes_with_weights
        self.heuristic_values = heuristic_values

    def beam_search(self, beam_width):
        start_node = 'S'
        queue = [['S']]
        visited = set()
        result = Result()
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            visited.add(node)

            if node == 'G':
                result.path = path
                return result

            result.extensions += 1
            for neighbor_dict in self.nodes_with_weights.get(node, []):
                for neighbor, weight in neighbor_dict.items():
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        queue.append(new_path)

            queue = sorted(queue, key=functools.cmp_to_key(self.compare_nodes()))
            queue = queue[:beam_width]

        result.path = path
        return result

    def calculate_path_cost(self, path):
        path_cost = 0
        for i in range(len(path) - 1):
            for neighbor_dict in self.nodes_with_weights.get(path[i], []):
                if path[i + 1] in neighbor_dict:
                    path_cost += neighbor_dict[path[i + 1]]
                    break
        return path_cost

    def compare_nodes(self):
        def comp(item1, item2):
            last_node_1 = item1[-1]
            heuristic_1 = self.heuristic_values.get(last_node_1, 0)
            cost_1 = self.calculate_path_cost(item1)

            last_node_2 = item2[-1]
            heuristic_2 = self.heuristic_values.get(last_node_2, 0)
            cost_2 = self.calculate_path_cost(item2)

            return (heuristic_1 + cost_1) - (heuristic_2 + cost_2)

        return comp