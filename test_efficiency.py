import functools
import time
import dfs
import bfs
import dikstra
import graph_generator
import top_sort
import top_sort_DFS


def logging(function):
    @functools.wraps(function)
    def wrapper(*args):
        N = 1000
        function(*args)
        function(*args)
        start_time = time.time()
        for _ in range(N):
            function(*args)
        end_time = time.time()
        work_time = end_time - start_time
        print(work_time / N, end="\n\n")

    return wrapper


@logging
def speed_dfs(graph, start):
    return dfs.DFS(graph, start)


@logging
def speed_bfs(a, start):
    return bfs.BFS(a, start)


@logging
def speed_top_sort_Kahn(a):
    return top_sort.TopologicalSort(a)


@logging
def speed_top_sort_DFS(a):
    return top_sort_DFS.DFS(a)


@logging
def speed_dijkstra(a, start):
    return dikstra.Dijkstra(a, start)


if __name__ == '__main__':
    best_data_100V = graph_generator.best_graph(100)
    best_data_500V = graph_generator.best_graph(500)
    best_data_800V = graph_generator.best_graph(800)
    worst_data_100V = graph_generator.worst_graph(100)
    worst_data_500V = graph_generator.worst_graph(500)
    worst_data_800V = graph_generator.worst_graph(800)
    rnd_data_100V = graph_generator.random_graph(100)
    rnd_data_500V = graph_generator.random_graph(500)
    rnd_data_800V = graph_generator.random_graph(800)
    # best_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.best_graph(100), 2)
    # worst_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.worst_graph(100), 2)
    # rnd_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.random_graph(100), 2)
    # best_weighted_graph_16KB = graph_generator.weighted_graph(graph_generator.best_graph(500), 2)
    # worst_weighted_graph_16KB = graph_generator.weighted_graph(graph_generator.worst_graph(500), 2)
    # rnd_weighted_graph_16KB = graph_generator.weighted_graph(graph_generator.random_graph(500), 2)
    # best_weighted_graph_32KB = graph_generator.weighted_graph(graph_generator.best_graph(800), 2)
    # worst_weighted_graph_32KB = graph_generator.weighted_graph(graph_generator.worst_graph(800), 2)
    # rnd_weighted_graph_32KB = graph_generator.weighted_graph(graph_generator.random_graph(800), 2)
    print("DFS")
    speed_dfs(best_data_100V, 0)
    speed_dfs(worst_data_100V, 0)
    speed_dfs(rnd_data_100V, 0)
    speed_dfs(best_data_500V, 0)
    speed_dfs(worst_data_500V, 0)
    speed_dfs(rnd_data_500V, 0)
    speed_dfs(best_data_800V, 0)
    speed_dfs(worst_data_800V, 0)
    speed_dfs(rnd_data_800V, 0)
    print("BFS")
    speed_bfs(best_data_100V, 0)
    speed_bfs(worst_data_100V, 0)
    speed_bfs(rnd_data_100V, 0)
    speed_bfs(best_data_500V, 0)
    speed_bfs(worst_data_500V, 0)
    speed_bfs(rnd_data_500V, 0)
    speed_bfs(best_data_800V, 0)
    speed_bfs(worst_data_800V, 0)
    speed_bfs(rnd_data_800V, 0)
    print("Topological sort by Kahn")
    speed_top_sort_Kahn(best_data_100V)
    speed_top_sort_Kahn(worst_data_100V)
    speed_top_sort_Kahn(rnd_data_100V)
    speed_top_sort_Kahn(best_data_500V)
    speed_top_sort_Kahn(worst_data_500V)
    speed_top_sort_Kahn(rnd_data_500V)
    speed_top_sort_Kahn(best_data_800V)
    speed_top_sort_Kahn(worst_data_800V)
    speed_top_sort_Kahn(rnd_data_800V)
    print("Topological sort on DFS")
    speed_top_sort_DFS(best_data_100V)
    speed_top_sort_DFS(worst_data_100V)
    speed_top_sort_DFS(rnd_data_100V)
    speed_top_sort_DFS(best_data_500V)
    speed_top_sort_DFS(worst_data_500V)
    speed_top_sort_DFS(rnd_data_500V)
    speed_top_sort_DFS(best_data_800V)
    speed_top_sort_DFS(worst_data_800V)
    speed_top_sort_DFS(rnd_data_800V)
    # print("Dijkstra")
    # speed_dijkstra(best_weighted_graph_8KB, 0)
    # speed_dijkstra(worst_weighted_graph_8KB, 0)
    # speed_dijkstra(rnd_weighted_graph_8KB, 0)
    # speed_dijkstra(best_weighted_graph_16KB, 0)
    # speed_dijkstra(worst_weighted_graph_16KB, 0)
    # speed_dijkstra(rnd_weighted_graph_16KB, 0)
    # speed_dijkstra(best_weighted_graph_32KB, 0)
    # speed_dijkstra(worst_weighted_graph_32KB, 0)
    # speed_dijkstra(rnd_weighted_graph_32KB, 0)
    print("OK")
