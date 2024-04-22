import matplotlib.pyplot as plt

def make_dendogram(final_cluster: list, history: list):
    max_value = history[-1][2]
    max_tick = max_value/len(final_cluster)
    x_ticks = [i*10 for i in range(len(final_cluster))]

    fig, ax = plt.subplots()
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(final_cluster)
    for item in ax.axes.get_xticklabels():
        item.set_rotation(90)
    
    new_clusters = []
    new_heights = []

    # work bottom to top
    for item in history:
        cluster_from, cluster_to, distance = item
        new_cluster = cluster_from + cluster_to
        new_clusters.append(new_cluster)
        new_heights.append(distance)

        # beginning of top line
        line_start = 0
        for point in cluster_from:
            index = final_cluster.index(point)
            line_start += x_ticks[index]
        line_start /= len(cluster_from)

        # end of top line
        line_end = 0
        for point in cluster_to:
            index = final_cluster.index(point)
            line_end += x_ticks[index]
        line_end /= len(cluster_to)

        # draw top line
        plt.plot([line_start, line_end], [distance, distance], color="black")

        # draw vertical left line
        if len(cluster_from) > 1:
            index = new_clusters.index(cluster_from)
            starting_height = new_heights[index]
            plt.plot([line_start, line_start], [starting_height, distance], color="black")
        else:
            plt.plot([line_start, line_start], [0, distance], color="black")
        
        # draw certical right line
        if len(cluster_to) > 1:
            index = new_clusters.index(cluster_to)
            starting_height = new_heights[index]
            plt.plot([line_end, line_end], [starting_height, distance], color="black")
        else:
            plt.plot([line_end, line_end], [0, distance], color="black")

        # draw point on the line to show connection
        mid_point = (line_start + line_end) / 2
        plt.plot(mid_point, distance, "ro")
        plt.text(mid_point, distance, f"{round(distance, 4)}", verticalalignment='bottom', horizontalalignment='center')

    plt.show()




