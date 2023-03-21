import matplotlib.pyplot as plt

if __name__ == "__main__":
    data_size = [100, 500, 800]
    fig, ax = plt.subplots()
    fig.set_size_inches(8, 6)
    times_best_data_dfs = [0.0, 8.001327514648438e-06, 0.0]
    times_best_data_bfs = [2.0003318786621095e-06, 0.0005889711380004883,
                           0.001210303544998169]
    times_best_data_Kahn = [6.531333923339844e-05, 0.00022072839736938477,
                            0.00038260388374328615]
    times_best_data_DFS = [5.700278282165527e-05, 0.00028803515434265136,
                           0.0004900701045989991]
    plt.xlabel("Best Data Size Vertices")
    plt.ylabel("Time")
    plt.scatter(data_size, times_best_data_dfs, c='k')
    plt.scatter(data_size, times_best_data_bfs, c='g')
    plt.scatter(data_size, times_best_data_Kahn, c='m')
    plt.scatter(data_size, times_best_data_DFS, c='r')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='r')
    fig2, ax2 = plt.subplots()
    fig2.set_size_inches(8, 6)
    times_worst_data_dfs = [0.0007747426033020019, 0.020506824493408203,
                            0.05278366017341614]
    times_worst_data_bfs = [0.0009801149368286132, 0.030884692668914793,
                            0.07709436774253846]
    times_worst_data_Kahn = [0.0018764338493347168, 0.05718257594108581,
                             0.15880903816223144]
    times_worst_data_DFS = [0.0007530534267425537, 0.019987739324569702,
                            0.05616207075119019]
    plt.xlabel("Worst Data Size Vertices")
    plt.ylabel("Time")
    plt.scatter(data_size, times_worst_data_dfs, c='k')
    plt.scatter(data_size, times_worst_data_bfs, c='g')
    plt.scatter(data_size, times_worst_data_Kahn, c='m')
    plt.scatter(data_size, times_worst_data_DFS, c='r')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='r')
    fig3, ax3 = plt.subplots()
    fig3.set_size_inches(8, 6)
    times_rnd_data_dfs = [0.0003196656703948975, 0.008573618173599242,
                          0.029325751781463624]
    times_rnd_data_bfs = [0.0004610333442687988, 0.011608999490737916,
                          0.03657220387458801]
    times_rnd_data_Kahn = [0.0007420949935913086, 0.023712504148483277,
                           0.06184373736381531]
    times_rnd_data_DFS = [0.0003170084953308106, 0.009530075550079346,
                          0.02908650064468384]
    plt.xlabel("Random Data Size Vertices")
    plt.ylabel("Time")
    plt.scatter(data_size, times_rnd_data_dfs, c='k')
    plt.scatter(data_size, times_rnd_data_bfs, c='g')
    plt.scatter(data_size, times_rnd_data_Kahn, c='m')
    plt.scatter(data_size, times_rnd_data_DFS, c='r')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='r')
    plt.show()
    fig4, ax4 = plt.subplots()
    fig4.set_size_inches(8, 6)
    mem_best_data_dfs = [88, 88, 88]
    mem_best_data_bfs = [88, 88, 88]
    mem_best_data_Kahn = [920, 4216, 6936]
    mem_best_data_DFS = [920, 4216, 6936]
    plt.xlabel("Worst Data Size Vertices")
    plt.ylabel("Memory (bytes)")
    plt.scatter(data_size, mem_best_data_dfs, c='k')
    plt.scatter(data_size, mem_best_data_bfs, c='g')
    plt.scatter(data_size, mem_best_data_Kahn, c='m')
    plt.scatter(data_size, mem_best_data_DFS, c='r')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='r')
    fig5, ax5 = plt.subplots()
    fig5.set_size_inches(8, 6)
    mem_worst_data_dfs = [920, 4216, 6936]
    mem_worst_data_bfs = [920, 4216, 6936]
    mem_worst_data_Kahn = [56, 56, 56]
    mem_worst_data_DFS = [920, 4216, 6936]
    plt.xlabel("Worst Data Size KB")
    plt.ylabel("Memory (bytes)")
    plt.scatter(data_size, mem_worst_data_dfs, c='k')
    plt.scatter(data_size, mem_worst_data_bfs, c='g')
    plt.scatter(data_size, mem_worst_data_Kahn, c='m')
    plt.scatter(data_size, mem_worst_data_DFS, c='r')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='r')
    fig6, ax6 = plt.subplots()
    fig6.set_size_inches(8, 6)
    mem_rnd_data_dfs = [920, 4216, 6936]
    mem_rnd_data_bfs = [920, 4216, 6936]
    mem_rnd_data_Kahn = [56, 56, 56]
    mem_rnd_data_DFS = [920, 4216, 6936]
    plt.xlabel("Random Data Size KB")
    plt.ylabel("Memory (bytes)")
    plt.scatter(data_size, mem_rnd_data_dfs, c='k')
    plt.scatter(data_size, mem_rnd_data_bfs, c='g')
    plt.scatter(data_size, mem_rnd_data_Kahn, c='m')
    plt.scatter(data_size, mem_rnd_data_DFS, c='r')
    plt.figtext(0, 0.005, "DFS", fontsize=10, color='k')
    plt.figtext(0.05, 0.005, "BFS", fontsize=10, color='g')
    plt.figtext(0.1, 0.005, "TopSort by Kahn", fontsize=10, color='m')
    plt.figtext(0.28, 0.005, "TopSort on DFS", fontsize=10, color='r')
    plt.show()
