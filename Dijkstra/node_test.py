__author__ = 'wbarbour1'

from Node_network_d import Network, Node

netw_t = Network("003")

def exec():
    pass

nt = netw_t.n1
list_test = [nt]
print(list_test.count(nt))
print(list_test.count(Node(1,[],[],1)))
