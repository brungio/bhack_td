# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:40:57 2022

@author: marieplgt,chris-zielinski
"""
	
# In[set environment]:
import scipy as sc
from scipy import io
import numpy as np
import time

def compute_dist(dat, type='cosine'):
    """Return distance using scipy function
    Parameters
    ----------
    dat : multidimensional array
    type: str
        type of distance: 'cosine' or 'euclidian'
        
    Returns
    -------
    dist: the computed distance
    """
    # get the data shape
    ndim = np.shape(dat)
    # init the output
    n_pair = int(ndim[0]*(ndim[0]-1)/2)
    dist = np.zeros((n_pair, ndim[2], ndim[3]))
    # loop // dim
    for i in range(ndim[2]):
        for j in range(ndim[3]):
            dist[:, i, j] = sc.spatial.distance.pdist(dat[:,:,i,j], metric=type)
    return dist

if __name__ == '__main__':
    # load the matlab data
    fname = 'C:\\home\oprojects\\brainhack22\\bhack_td\\results\\bhack_task_02_output_temporalfolding.mat'
    tmp = io.loadmat(fname)

    Xs = tmp['Xs'][0] 
    del tmp
    # distance computation for the 3 data types

    start_time = time.perf_counter()
    # acoustic data # (489, 3, 90, 10)
    # 90: predictor
    # 10: timechunks
    dist_ac = compute_dist(Xs[0], 'cosine')
    print("Shape: acoustic= {}".format(np.shape(dist_ac)))
    # sem data # (489, 1536, 18, 10)
    dist_sem = compute_dist(Xs[1], 'cosine')
    print("Shape: sem= {}".format(np.shape(dist_sem)))
    # eeg data # (489, 3, 3, 10)
    dist_eeg = compute_dist(Xs[2], 'euclidean')
    print("Shape: eeg= {}".format(np.shape(dist_eeg)))
    finish_time = time.perf_counter()
    print("Computing time {} s".format(finish_time-start_time))
    
    Ds = [[dist_ac], [dist_sem], [dist_eeg]]
    # io.savemat('C:\\home\oprojects\\brainhack22\\test_sem.mat', {'sem': dist_sem})














    
    