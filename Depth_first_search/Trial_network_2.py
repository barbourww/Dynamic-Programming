__author__ = 'wbarbour1'

from Node_delay_v1 import Network, Node

netw = Network("001")


def ex():
    n1 = Node(1, [], [2, 3, 4], 1)
    n2 = Node(2, [1], [5], 1)
    n3 = Node(3, [1], [6], 4)
    n4 = Node(4, [1], [6], 5)
    n5 = Node(5, [2], [7], 7)
    n6 = Node(6, [3, 4], [7, 8], 3)
    n7 = Node(7, [5, 6], [9], 2)
    n8 = Node(8, [6], [9], 3)
    n9 = Node(9, [7, 8], [], 1)
    netw.add_node([n1, n2, n3, n4, n5, n6, n7, n8, n9])
    print("Network: ")
    netw.print_network()
    print("")
    print("")


ex()
print("Minimize function:")
print("")
print("Total path delay :",netw.minimize_path(1, 9))