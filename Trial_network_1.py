from Node_delay_v1 import Network, Node

netw = Network("001")


def ex():
    n1 = Node(1, [], [2, 3], 1)
    n2 = Node(2, [1], [4], 6)
    n3 = Node(3, [1], [4], 4)
    n4 = Node(4, [2, 3], [], 1)
    netw.add_node([n1, n2, n3, n4])
    print("Network: ")
    netw.print_network()
    print("")
    print("")


ex()
print("Minimize function:")
print("")
print("Total path delay :",netw.minimize_path(1, 4))

""" OUTPUT:
/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 "/Users/wbarbour1/Documents/Dropbox/CEE/Python/Dynamic Programming/Trial_network_1.py"
Network:
Node ID:  0
Upstream nodes:  []
Downstream nodes:  []
Delay:  0
Node ID:  1
Upstream nodes:  []
Downstream nodes:  [2, 3]
Delay:  1
Node ID:  2
Upstream nodes:  [1]
Downstream nodes:  [4]
Delay:  6
Node ID:  3
Upstream nodes:  [1]
Downstream nodes:  [4]
Delay:  4
Node ID:  4
Upstream nodes:  [2, 3]
Downstream nodes:  []
Delay:  1


Minimize function:

Minimize between  1  and  4
Upstream node set:  [2, 3]
Assess node:  2
Minimize between  1  and  2
Upstream node set:  [1]
Assess node:  1
Minimize between  1  and  1
Upstream node set:  []
New best route:  1
New best route:  7
Assess node:  3
Minimize between  1  and  3
Upstream node set:  [1]
Assess node:  1
Minimize between  1  and  1
Upstream node set:  []
New best route:  1
New best route:  5
Total path delay : 6

Process finished with exit code 0
"""