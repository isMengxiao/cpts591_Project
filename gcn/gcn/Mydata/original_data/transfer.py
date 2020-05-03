# -*- coding: utf-8 -*-

import pickle as pkl
import collections as col
import numpy as np
import pandas as pd
from scipy.sparse.csr import csr_matrix

filenames = ['cornell', 'texas', 'washington', 'wisconsin']

for filename in ['cornell']:
    data1 = pd.read_table('{}.cites'.format(filename), sep=' ', header=None)
    data2 = pd.read_table('{}.content'.format(filename), sep='\t', header=None)
    namelist = []
    for name in data2[0]:
        namelist.append(name)
    namelist = tuple(namelist)

    web1 = []
    web2 = []
    #  ------------------graph----------------------
    graph = col.defaultdict(list)
    for k in range(len(data1)):
        i = namelist.index(data1[0][k])
        j = namelist.index(data1[1][k])
        if i != j:
            web1.append(namelist.index(data1[0][k]))
            web2.append(namelist.index(data1[1][k]))
            graph[i].append(j)

    #  ------------------x--------------------------
    allx = csr_matrix((np.ones(len(web1)), (web1, web2)), shape=(len(data2), len(data2)))
    print(allx)

    print(allx.shape[1])
    #  ------------------y--------------------------
    ally = np.array


