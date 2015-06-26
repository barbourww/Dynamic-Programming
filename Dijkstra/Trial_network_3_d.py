__author__ = 'wbarbour1'

from Node_network_d import Network, Node_d

netw = Network("001")


def ex():
    n1 = Node_d(1, [], [2, 3], 1)
    n2 = Node_d(2, [1], [4, 5, 6], 3)
    n3 = Node_d(3, [1], [7, 8], 6)
    n4 = Node_d(4, [2], [9], 1)
    n5 = Node_d(5, [2, 11], [9, 11], 3)
    n6 = Node_d(6, [2], [10], 5)
    n7 = Node_d(7, [3], [10], 3)
    n8 = Node_d(8, [3], [10, 12], 5)
    n9 = Node_d(9, [4, 5], [11, 13], 6)
    n10 = Node_d(10, [6, 7, 8], [11], 4)
    n11 = Node_d(11, [9, 10, 5], [13, 14, 5], 2)
    n12 = Node_d(12, [8], [14], 6)
    n13 = Node_d(13, [9, 11], [15], 4)
    n14 = Node_d(14, [11, 12], [15], 3)
    n15 = Node_d(15, [13, 14], [], 2)
    netw.add_node([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15])
    print("")
    print("Network: ")
    netw.print_network()
    print("")
    print("")


ex()
print("Minimize function:")
print("")
print("Total path delay :", netw.minimize_path(1, 15))
