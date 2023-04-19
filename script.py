from heapq import heappop, heappush
from manhattan_graph import manhattan_graph, thirty_eighth_and_fifth, grand_central_station
from math import sqrt, inf

def heuristic(sample_node, target_node):
    x_distance = abs(sample_node.position[0] - target_node.position[0])
    y_distance = abs(sample_node.position[1] - target_node.position[1])
    return x_distance + y_distance

def a_star(graph, start, terget):
    print("Start A* algorithem")
    paths_and_distence = {}
    count = 0
    for vertix in graph:
        paths_and_distence[vertix] = [inf, [start.name]]
    
    paths_and_distence[start][0] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore and paths_and_distence[terget][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[current_vertex]:
            count += 1
            new_distance = current_distance + edge_weight + heuristic(neighbor, terget)
            new_path = paths_and_distence[current_vertex] + [neighbor.name]

            if new_distance < paths_and_distence[neighbor][0]:
                paths_and_distence[neighbor][0] = new_distance
                paths_and_distence[neighbor][1] = new_path

                heappush(vertices_to_explore, (new_distance, neighbor))
    print("Found a path from {0} to {1} in {2} steps: ".format(start.name, terget.name, count), paths_and_distence[terget][1])
    return paths_and_distence[terget][1]

a_star(manhattan_graph, thirty_eighth_and_fifth, grand_central_station)