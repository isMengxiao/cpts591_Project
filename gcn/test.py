# -*- coding: utf-8 -*-

import numpy as np
import pickle as pkl
import scipy.sparse as sp
import networkx as nx
from scipy.sparse.linalg.eigen.arpack import eigsh
from utils import *


names = ['x', 'y', 'tx', 'ty', 'allx', 'ally', 'graph']
objects = []
for i in range(len(names)):
    with open("data/ind.cora.{}".format(names[i]), 'rb') as f:
        objects.append(pkl.load(f, encoding='latin1'))

test_index_reorder = parse_index_file("data/ind.cora.test.index")
test_index_range = np.sort(test_index_reorder)
x, y, tx, ty, allx, ally, graph = tuple(objects)

'''
print("-----------print x------------")
print(x)
print("-----------print y------------")
print(y)
print("\n\n--------------------print tx____________\n")
print(tx)
print("\n\n--------------------print ty------------\n")
print(ty)
print("\n\n--------------------print allx____________\n")
print(allx)
print("\n\n--------------------print ally------------\n")
print(ally)
print("\n\n----------------------graph-------------\n")
print(graph)
print("\n\n----------------------index-------------\n")
print(test_index_reorder)
print("\n\n-----------------rang-------------\n")
print(test_index_range)
'''

print("\n\n-----------------------------allx------------\n")
print(type(allx))
print(type(ally))
print(type(test_index_reorder))
