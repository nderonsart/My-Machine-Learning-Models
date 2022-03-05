#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
My K-means clustering

@author: deronsart
"""

from random import sample
import cluster as clst



def k_means(points, k):
    ''' 
        Function that classifies the points in k clusters
            Params: a list of points and the number of clusters
            Return: the list of clusters
    '''
    assert k > 0
    
    k_centers = sample(points,k)
    
    clusters = []
    del_points = []
    
    for i in range(k):
        clusters.append(clst.Cluster([k_centers[i]]))
        del_points.append(k_centers[i])
        points.remove(k_centers[i])
    
    
    stop = False
    while not stop:
        stop = True
        
        for ind in range(len(points)):
                
            distance_min = clusters[0].center()
            ind_dist_min = 0
            for i in range(1,len(clusters)):
                if (points[ind].distance(clusters[i].center()) 
                     < points[ind].distance(distance_min)):
                    distance_min=clusters[i].center()
                    ind_dist_min=i
            
            if (not clusters[ind_dist_min].belongs(points[ind])):
                for i in range(len(clusters)):
                    if clusters[i].belongs(points[ind]):
                        clusters[i].delete(points[ind]) 
                clusters[ind_dist_min].append(points[ind])
                stop = False
        
        while (len(del_points) > 0):
            points.append(del_points[0])
            del del_points[0]
    
    return clusters


