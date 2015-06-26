__author__ = 'wbarbour1'


class Node_d:
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
        print("Aux parameter: ", self.aux)


class Network:
    """This class constructs nodes and indexes them by their ID numbers"""
    n1 = Node_d(0, [], [], 0)
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

    def get_node(self, ref_id) -> Node_d:
        """
            Finds and returns the node with specified node_ID from Network's node_ref.
            Returns null node if not found.
            :rtype : Node_d
            """
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
            n.aux = 999999
            unvisited.append(n)
        print("All nodes' aux parameter initialized to 999999")
        print("")
        current = self.get_node(snr)
        current.aux = current.delay
        print("Current: ", current)
        current.print_node()
        print("")
        while True:
            print("Current's downstream: ", current.downstream)
            print("")
            for n_ref in current.downstream:
                n = self.get_node(n_ref)
                print("Downstream node: ", n)
                n.print_node()
                if unvisited.count(n) != 0:
                    print("Node unvisited")
                    d = current.aux + n.delay
                    print("Test tentative distance: ", d)
                    print("Against: ", n.aux)
                    if d < n.aux:
                        n.aux = d
                        print("New tentative distance: ", n.aux)
                    else:
                        print("Keep old tentative distance")
                else:
                    print("Already visited")
                print("")
            unvisited.remove(current)
            print("Removed from unvisited: ", current)
            current.print_node()
            print("")
            next_current = unvisited[1] #disregard null node at unvisited[0]
            print("First node in unvisited: ", next_current)
            next_current.print_node()
            low_tent = next_current.aux
            for next_n in unvisited:
                print("Evaluate node #", next_n.node_id, "for lower tentative delay")
                if next_n.aux < low_tent:
                    low_tent = next_n.aux
                    print("New lowest tentative delay: ", low_tent)
                    next_current = next_n
            current = next_current
            print("")
            print("New current node: ", current)
            current.print_node()
            if current.node_id == fnr:
                print("")
                print("*****************************************")
                print("Current node is final node...terminating.")
                print("*****************************************")
                return current.aux
