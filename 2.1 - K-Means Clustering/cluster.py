#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class that represents a cluster

@author: deronsart
"""

import point as pt



class Cluster:
    
    def __init__(self, points = []):
        ''' 
            Constructor of the Cluster class
                Params: a list of points
        '''
        self.__points = points
    
    
    def center(self):
        ''' 
            Function that calculates the coordinates of the center of the cluster
                Return: a point
        '''
        sum_abs = 0
        sum_ord = 0
        for i in range(len(self.__points)):
            sum_abs += self.__points[i].abscissa()
            sum_ord += self.__points[i].ordinate()
        return pt.Point(sum_abs/len(self.__points), sum_ord/len(self.__points))
    
    
    def get_points(self):
        ''' 
            Function that returns the list of points of the cluster
                Return: the list of points
        '''
        l = []
        for i in range(len(self.__points)):
            l.append((self.__points[i].abscissa(),self.__points[i].ordinate()))
        return l
        
    
    def append(self, point):
        ''' 
            Function that adds a point to the cluster
                Params: the point
        '''
        self.__points.append(point)
    
    
    def delete(self, point):
        ''' 
            Function that removes a point from the cluster
                Params: the point
        '''
        
        i=0
        while (i < len(self.__points)):
            if (self.__points[i] == point):
                del self.__points[i]
            i+=1
    
    
    def belongs(self, point):
        ''' 
            Function that indicates if a point belogs to the cluster
                Params: the point
                Return: True or False
        '''
        
        if (point in self.__points):
            return True
        
        return False


