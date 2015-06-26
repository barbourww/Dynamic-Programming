__author__ = 'wbarbour1'

from Graph import fw_graph

gr = fw_graph("002", 6)


def g_make():
    gr.add_connections(1, [[2, 3], [5, -4], [3, 8]])
    gr.add_connections(2, [[4, 1], [5, 7]])
    gr.add_connections(3, [[2, 4]])
    gr.add_connections(4, [[1, 2], [3, -5]])
    gr.add_connections(5, [[4, 6], [6, 1]])
    gr.add_connections(6, [[1, 4], [4, 3]])
    gr.print_mat(gr.mat)


g_make()
print(gr.fw_minimize())
