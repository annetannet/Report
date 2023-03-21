import functools
import time
import dfs
import bfs
import dikstra
import graph_generator
import top_sort
import top_sort_DFS
import sys


def logging(function):
    @functools.wraps(function)
    def wrapper(*args):
        N = 1000
        function(*args)
        function(*args)
        function(*args)

        real_times = [0] * N
        for i in range(N):
            start_time = time.time()
            function(*args)
            end_time = time.time()
            real_times[i] = end_time - start_time
        average_time = sum(real_times) / N
        digressions = [0] * N
        for i in range(N):
            digressions[i] = abs(real_times[i] - average_time)
        aver_digression = sum(digressions) / N  # отклонение
        print("aver digression", aver_digression)
        return average_time

    return wrapper


@logging
def speed_dfs(graph, start=0):
    return dfs.DFS(graph, start)


@logging
def speed_bfs(a, start=0):
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


def test_algorithm(args, function):
    all_times = []
    for i in args:
        all_times.append(function(i))
    return all_times


def test(function):
    dots_counts = [100, 300, 500, 800, 1200]
    args = []
    for i in dots_counts:
        args.append(function(i))
    test_ans = []
    test_ans.append(test_algorithm(args, speed_dfs))
    test_ans.append(test_algorithm(args, speed_bfs))
    test_ans.append(test_algorithm(args, speed_top_sort_Kahn))
    test_ans.append(test_algorithm(args, speed_top_sort_DFS))
    return test_ans


def get_data():
    sys.setrecursionlimit(10000)
    ans = []
    ans.append(test(graph_generator.best_graph))
    return ans


if __name__ == '__main__':
    print(*get_data(), sep='\n')
