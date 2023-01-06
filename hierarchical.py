import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree, cut_tree
from matplotlib import pyplot as plt

# X = context_embs
X= p

linkage_matrix = linkage(X, "single")
clusters = cut_tree(linkage_matrix, n_clusters=None)

# insert column for the case, where every element is its own cluster
clusters = np.insert(clusters, clusters.shape[1], range(clusters.shape[0]), axis=1)
# transpose matrix
clusters = clusters.T

# for row in clusters[::-1]:
for row in clusters:
    # create empty dictionary
    groups = {}
    for i, g in enumerate(row):
        if g not in groups:
            # add new key to dict and assign empty set
            groups[g] = set([])
        # add to set of certain group
        groups[g].add(i)
    print(list(groups.values()))
    large_group = []
    for each in groups.values():
      small_group = []
      for each_each in each:
        # small = part_model_syn[each_each]
        
        small = new_matrix[each_each]
        small_group.append(small)
      large_group.append(small_group)
    print(large_group)
      
