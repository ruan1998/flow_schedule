import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np

import os
np.set_printoptions(formatter={'float_kind':'{:.3f}'.format})

class NetFlow:
    
    def __init__(self, file_path=None):

        if file_path:
            self.read(file_path)
        self.graph = None
        self._set_transform_matrix()
        
    def read(self, file_path):
        self._raw_data = genfromtxt(file_path, delimiter=',', dtype='int')
        
        self.nodes_id = np.unique(self._raw_data)
        self.node_num = len(self.nodes_id)
        self._data_normalize()
        
    def _data_normalize(self):
        # change the first id of node to 0 if it isn't, other node change at the same time
        min_node_id = self.nodes_id.min()
        if  min_node_id != 0:
            self.nodes_id -= min_node_id
            self._raw_data -= min_node_id

    def __repr__(self):
        return str(self._raw_data)
        
    @property
    def data(self):
        return self._raw_data
    
    def sample(self, num, init, max_T=10):
        # init should be dict type with pair of id and probability of init state
        init_S, init_P = list(zip(*init.items()))
        is_end = lambda t, state: (t >= max_T - 1) or (state in self._end_id)
        def sample_one(t=0, states=None):
            if t == 0:
                states = [np.random.choice(init_S, p=init_P)]
            else:
                states.append(np.random.choice(self.nodes_id, p=self.matrix[states[-1]]))
                 
            if is_end(t, states[-1]):
                return states
            # tail recursive
            return sample_one(t+1, states)
            
        self.samples = [sample_one() for _ in range(num)]
        
        return self.samples
        
    def draw(self):
        if not self.graph:
            self.graph = nx.DiGraph()
            self.graph.add_nodes_from(self.nodes_id)
            self.graph.add_edges_from(self._raw_data.tolist())
            
            pos = nx.circular_layout(self.graph)
        nx.draw_networkx(self.graph, pos=pos)
        plt.show()
    
    def _set_transform_matrix(self):
        self._matrix = np.zeros((self.node_num, self.node_num))
        
        row_id, col_id = self._raw_data.T
        self._matrix[row_id, col_id] = 1
        # ${problem}$, now we are uniform distribution
        row_sum = self._matrix.sum(axis=1)[:, None]
        self._matrix = np.divide(self._matrix, row_sum, where=row_sum!=0)
        
        self._end_id = self.nodes_id[row_sum.flatten() == 0]
        
    @property
    def matrix(self):
        return self._matrix

def insert_front(num, ls):
    '''
        ls should be a sorted list in ascending order 
    '''
    def insert_binary(ls=ls, idx=0):
        middle_idx = len(ls) // 2
        if middle_idx == 0:
            return idx
        left_part, right_part = ls[:middle_idx], ls[middle_idx:]
        if left_part[-1] > num:  
            return insert_binary(left_part, idx)
        idx += middle_idx
        return insert_binary(right_part, idx)
    
    idx = insert_binary()
    ls.insert(idx, num)

if __name__ == '__main__':
    
    data_folder = 'data'
    network_diagram1_path = os.path.join(data_folder, 'diagram1.csv')

    custom_net = NetFlow(network_diagram1_path)

    print(custom_net.matrix)