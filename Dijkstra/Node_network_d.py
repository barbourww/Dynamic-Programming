__author__ = 'wbarbour1'


class Node:
    """This class represents a single node of a larger network.
    A network is defined by node connections.
    Parameters:
    Node(int node_id, int list [upstream connections], int list [downstream connections], int delay)
    """

    def __init__(self, node_id, upstream, downstream, delay):
        self.node_id = node_id
        assert(isinstance(upstream, list)), "Can't reference null node as part of network. " \
                               "Did you mean that the value is empty []?"
        self.upstream = upstream
        assert(isinstance(downstream, list)), "Can't reference null node as part of network. " \
                               "Did you mean that the value is empty []?"
        self.downstream = downstream
        self.delay = delay
        self.aux = None

    def print_node(self):
        print("Node ID: ", self.node_id)
        print("Upstream nodes: ", self.upstream)
        print("Downstream nodes: ", self.downstream)
        print("Delay: ", self.delay)


class Network:
    """This class constructs nodes and indexes them by their ID numbers"""
    n1 = Node(0, [], [], 0)
    node_ref = [n1]
    node_count = 0

    def __init__(self, net_id):
        self.net_id = net_id

    # TODO add check method to point out pathway errors (upstream/downstream continuity)

    def add_node(self, nodes):
        """Adds list of nodes to network (format with brackets even if singular)"""
        for n in nodes:
            self.node_ref.append(n)
            self.node_count += 1

    def get_node(self, ref_id):
        for i in self.node_ref:
            if i.node_id == ref_id:
                return i
        return self.n1

    def print_network(self):
        for i in self.node_ref:
            i.print_node()
        return True

    def minimize_path(self, snr, fnr):
        unvisited = []
        for n in self.node_ref:
            self.get_node(n).aux = 999999
            unvisited.append(n)
        current = self.get_node(snr)
