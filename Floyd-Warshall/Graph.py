__author__ = 'wbarbour1'

class fw_graph:
    """
        This class initializes and supports definition of a node-edge
        graph for path optimization using matrix manipulation
        Matrix organized as list of length n (dimension i) containing
        lists of length n (dimension j).
        Connection i -> j referenced as self.mat[i][j]

            Dim j >>
        [
            [0, 9999, 9999, 9999]
            [9999, 0, 9999, 9999]
            [9999, 9999, 0, 9999]
            [9999, 9999, 9999, 0]
        ]
         ^^
        Dim i

    """
    def __init__(self, g_id, num_nodes):
        self.g_id = g_id
        self.n = num_nodes
        self.mat = None
        self.allocate_matrix()
        self.print_mat(self.mat)

    def allocate_matrix(self):
        """
        Constructs n x n sized matrix with all i -> j connections
        initialized to infinity (9999 used) and all i -> i connections
        initialized to zero
        """
        new_mat = []
        for i in range(self.n):
            t = []
            for j in range(self.n):
                if j == i:
                    t.append(0)
                else:
                    t.append(9999)
            new_mat.append(t)
        self.mat = new_mat

    def change_size(self, new_num_nodes):
        self.n = new_num_nodes
        self.allocate_matrix()

    def add_connection(self, node_i, node_j, cost):
        self.mat[node_i][node_j] = cost

    def add_connections(self, node, conn_list):
        """
        Adds list of connections FROM specified TO nodes listed
        in conn_list with format [[TO_1, C_1], [TO_2, C_2], [TO_n, C_n]]
        where C_n is the edge cost
        """
        assert(isinstance(conn_list, list)), \
            "Incorrect argument format. conn_list must be type (list)."
        assert(isinstance(conn_list[0], list)), \
            "Incorrect argument format. Members of conn_list must be type (list)."
        for conn in conn_list:
            self.mat[node-1][conn[0]-1] = conn[1]

    def print_mat(self, matr):
        print("[")
        for i in range(self.n):
            print(matr[i])
        print("]")

    def fw_minimize(self) -> list:
        """
        :rtype : list
        """
        min_mat = self.mat

        path_k = []
        for i in range(self.n):
            t = []
            for j in range(self.n):
                t.append(9999)
            path_k.append(t)
        print(path_k)
        for i in range(self.n):
            for j in range(self.n):
                if min_mat[i][j] < 9999 and min_mat[i][j] != 0:
                    path_k[i][j] = i+1
        print(path_k)

        for k in range(self.n):
            print("***** k =", k, "*****")
            for i in range(self.n):
                print("*** i =", i, "***")
                for j in range(self.n):
                    print("* j =", j, "*")
                    d_t = min_mat[i][k] + min_mat[k][j]
                    print("Distance from", i+1, "to", j+1, "via", k+1,"=", d_t)
                    if d_t < min_mat[i][j]:
                        print("Distance via", k+1, "is less than existing value of", min_mat[i][j],". Reassign.")
                        min_mat[i][j] = d_t
                        print("Path from", i+1, "to", j+1, "updated to", k+1)
                        path_k[i][j] = (k + 1)
                        print(path_k)
                    else:
                        print("Not less than existing")

        self.print_mat(min_mat)
        self.print_mat(path_k)
        return min_mat

