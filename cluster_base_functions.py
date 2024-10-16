from __future__ import division
import math 
import pandas as pd
import numpy as np
from scipy import stats
from sklearn import metrics
from scipy.optimize import linear_sum_assignment
def reorder_clustering_labels(primary_labels, alter_labels):
    cmtx = metrics.cluster.contingency_matrix(primary_labels, alter_labels)
    prim_labs = np.unique(primary_labels)
    prim_ind, alt_ind = linear_sum_assignment(-cmtx)
    nlabels = np.zeros_like(alter_labels)
    for pind in prim_ind:
        nlabels[alter_labels==alt_ind[pind]] = prim_labs[prim_ind[pind]]
    return nlabels

from itertools import combinations
def labels_to_adjacent_matrix(labels, ignore_lab=-1):
    num = len(labels)
    lab_list = np.unique(labels)
    mtx = np.zeros((num, num))
    for lab in lab_list:
        if lab==ignore_lab:
            continue
        idx = np.where(labels==lab)[0]
        cidx = [t for t in combinations(idx, 2)]
        for v in cidx:
            mtx[v] = 1
    mtx = mtx.T + mtx
    #
    idx = np.where(labels==ignore_lab)[0]
    mtx[idx] = np.nan
    mtx[:,idx] = np.nan
    return mtx