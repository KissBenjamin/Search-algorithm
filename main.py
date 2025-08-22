from branch_and_bound import BranchAndBound
import graph_building
import searches
from beam_search import BeamSearch
import time

def start_timer():
    return time.time()

def timer_result(start_time):
    result_with_four_decimal_point = "{:.4f}".format(time.time() - start_time)
    return f"{result_with_four_decimal_point}s"

def algorithms():
    while True:
        print('1, Breadth-first search')
        print('2, Depth-first search')
        print('3, Breach and Bound basic')
        print('4, Breach and Bound extended list')
        print('5, Breach and Bound heuristic')
        print('6, Breach and Bound A*')
        print('7, Hill climbing')
        print('8, Beam search')
        print('9, Best-first search')
        input_ = input('Melyik algoritmust szeretnéd megnézni? (0-val visszamehetsz a gráfokhoz)')
        if input_ == '0':
            break
        if not input_.isdigit():
            continue
        graph_index = int(input_)
        if graph_index < 1 or graph_index > 9:
            continue
        
        print()
        start = start_timer()
        match graph_index:
            case 1:
                
                searches.bfs(graph.nodes, 'S', 'G')
            case 2:
                searches.dfs(graph.nodes, 'S', 'G')
            case 3:
                basic = BranchAndBound(graph.nodes_with_weights, 'basic')
                print(str(basic.algorithm().__dict__))
            case 4:
                extended_list = BranchAndBound(graph.nodes_with_weights, 'extended list')
                print(str(extended_list.algorithm().__dict__))
            case 5:
                heuristic = BranchAndBound(graph.nodes_with_weights, 'heuristic', graph.heuristic_values)
                print(str(heuristic.algorithm().__dict__))
            case 6:
                a_star = BranchAndBound(graph.nodes_with_weights, 'A*', graph.heuristic_values)
                print(str(a_star.algorithm().__dict__))
            case 7:
                print(str(searches.hill_climing(graph).__dict__))
            case 8:
                beam_search = BeamSearch(graph.nodes_with_weights, graph.heuristic_values)
                print(str(beam_search.beam_search(2).__dict__))
            case 9:
                print(str(searches.best_first_search(graph).__dict__))
        print(timer_result(start))
        print()

graphs = graph_building.build_graphs()



while True:
    input_ = input('Melyik gráfot szeretnéd megnézni (1,2)? ')
    if not input_.isdigit():
        continue
    graph_index = int(input_)
    if graph_index < 1 or graph_index > 2:
        continue
        
    graph = graphs[graph_index-1]

    algorithms()