import functools
import dfs
import bfs
import dikstra
import top_sort
import top_sort_DFS
import sys
import graph_generator


def logging(function):
    @functools.wraps(function)
    def wrapper(*args):
        k = 0
        a = function(*args)
        for i in a:
            k += sys.getsizeof(a)  # bytes
        print(k, end="\n\n")
    return wrapper


@logging
def mem_dfs(graph, start):
    return dfs.DFS(graph, start)


@logging
def mem_bfs(a, start):
    return bfs.BFS(a, start)


@logging
def mem_top_sort_Kahn(a):
    return top_sort.TopologicalSort(a)


@logging
def mem_top_sort_DFS(a):
    return top_sort_DFS.DFS(a)


@logging
def mem_dijkstra(a, start):
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
    print("DFS")
    mem_dfs(best_data_100V, 0)
    mem_dfs(worst_data_100V, 0)
    mem_dfs(rnd_data_100V, 0)
    mem_dfs(best_data_500V, 0)
    mem_dfs(worst_data_500V, 0)
    mem_dfs(rnd_data_500V, 0)
    mem_dfs(best_data_800V, 0)
    mem_dfs(worst_data_800V, 0)
    mem_dfs(rnd_data_800V, 0)
    print("BFS")
    mem_bfs(best_data_100V, 0)
    mem_bfs(worst_data_100V, 0)
    mem_bfs(rnd_data_100V, 0)
    mem_bfs(best_data_500V, 0)
    mem_bfs(worst_data_500V, 0)
    mem_bfs(rnd_data_500V, 0)
    mem_bfs(best_data_800V, 0)
    mem_bfs(worst_data_800V, 0)
    mem_bfs(rnd_data_800V, 0)
    print("Topological sort by Kahn")
    mem_top_sort_Kahn(best_data_100V)
    mem_top_sort_Kahn(worst_data_100V)
    mem_top_sort_Kahn(rnd_data_100V)
    mem_top_sort_Kahn(best_data_500V)
    mem_top_sort_Kahn(worst_data_500V)
    mem_top_sort_Kahn(rnd_data_500V)
    mem_top_sort_Kahn(best_data_800V)
    mem_top_sort_Kahn(worst_data_800V)
    mem_top_sort_Kahn(rnd_data_800V)
    print("Topological sort on DFS")
    mem_top_sort_DFS(best_data_100V)
    mem_top_sort_DFS(worst_data_100V)
    mem_top_sort_DFS(rnd_data_100V)
    mem_top_sort_DFS(best_data_500V)
    mem_top_sort_DFS(worst_data_500V)
    mem_top_sort_DFS(rnd_data_500V)
    mem_top_sort_DFS(best_data_800V)
    mem_top_sort_DFS(worst_data_800V)
    mem_top_sort_DFS(rnd_data_800V)
    print("OK")