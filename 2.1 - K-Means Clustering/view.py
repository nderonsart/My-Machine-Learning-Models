#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for my K-Means Clustering Algorithm

@author: deronsart
"""

import matplotlib.pyplot as plt

from random import randint

import point as pt
from k_means import k_means



def k_means_vue(points, k):
    ''' 
        Function that allows to visualize the k clusters
            Params: a list of points and the number of clusters
    '''
    assert k<7
    
    plt.title('k-Means')
    plt.xlabel('Abscissa')
    plt.ylabel('Ordinate')
    
    colors = ['ro','bo','go','yo','mo','co','ko']
    
    clusters = k_means(points, k)
    
    for i in range(k):
        cluster = clusters[i].get_points()
        for j in range(len(cluster)):
            plt.plot(cluster[j][0], cluster[j][1], colors[i])
        
    plt.show()


def points_alea(n):
    ''' 
        Function that creates a list of n random points
            Params: the number of random points
            Return: the list of random points
    '''
    points = []
    for i in range(n):
        points.append(pt.Point(randint(0,15), randint(0,10)))
    return points



if __name__ == '__main__':
    points = points_alea(32)
    k = 4
    
    k_means_vue(points, k)


