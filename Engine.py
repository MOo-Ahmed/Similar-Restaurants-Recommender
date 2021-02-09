import pandas as pd
import numpy as np
import math
import pickle
import json

'''
get list of matching restaurants - sort them according to distance
'''

data = None

class RecommendationEngine :
    
    def __init__(self, combined, prefs, location, n):
        global data
        data = combined
        self.prefs = prefs
        self.n = n
        self.location = location

    def set_Dataset_Filename(self, file):
        self.dataset_filename = file
        
    def getNearestRestaurants(self, combined, x, y):
        distances = []
        n = len(combined)
        for i in range (n):
            d = math.sqrt((combined[i][2] - x)**2 + (combined[i][3] - y)**2)
            #id , distance , name
            pair = [combined[i][0], d, combined[i][1]]
            distances.append(pair)
        distances.sort(key=lambda x: x[1])
        l = []
        for i in range (self.n) :
            restaurant = [distances[i][0], distances[i][1], distances[i][2]]
            l.append(restaurant)
        
        return l

    def getMatchingRestaurants(self, prefs, data):
        match = []
        n = len(data[0])
        for i in range (n):
            ctg = data[2][i].split('/')
            for j in range (len(prefs)):
                if prefs[j] in ctg :
                    match.append([data[0][i] , data[1][i] , data[3][i], data[4][i] ])
                    break
        return match
    
    def run (self):

        #Get the matching restaurants
        match =  self.getMatchingRestaurants(self.prefs, data)
        #Get the nearest N 
        d = self.getNearestRestaurants(match, self.location[0] , self.location[1])
        print(d)

        











        
        
