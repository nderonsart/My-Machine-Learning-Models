#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class that represents a point

@author: deronsart
"""

from math import sqrt



class Point:
    
    def __init__(self, abscissa, ordinate):
        ''' 
            Constructor of the Point class
                Params: the abscissa and the ordinate of the point
        '''
        self.__abscissa = abscissa
        self.__ordinate = ordinate
    
    
    def __str__(self):
        ''' 
            Function that returns a string representation of the point
                Return: the string
        '''
        return "(" + str(self.__abs) + ", " + str(self.__ord) + ")"
        
    
    def abscissa(self):
        ''' 
            Function that returns the value of the abscissa of the point
                Return: the abscissa
        '''
        return self.__abscissa
    
    
    def ordinate(self):
        ''' 
            Function that returns the value of the ordinate of the point
                Return: the ordinate
        '''
        return self.__ordinate
    
    
    def distance(self, p2):
        ''' 
            Function that returns the distance between the point and p2
                Return: the distance
        '''
        return sqrt(abs(self.__abscissa - p2.abscissa())**2 + 
                    abs(self.__ordinate - p2.ordinate())**2)


