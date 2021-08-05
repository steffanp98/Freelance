# -*- coding: utf-8 -*-
"""centroidAlgo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z40nRj3q9yRdviwXvZhSUeh0TNC4S6P1
"""

#centroid object detection algo which will handle the object detecton and tracking system
 #updates obj IDS - reg new obj ID - deregisters old ones

#import libs 
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

#defining the tracker class 
class centroidTracker:
  #defining init function
  def __init__ (self, maxDisappeared = 50, maxDistance = 50):
    #inistialise the unique object id 
    self.nextObjectID = 0
    #mapping of the obj id will be stored in a dict
    self.objects = OrderedDict()
    #amount of times that an obj has dissapeared will also be stored in dict
    self.disappeared = OrderedDict()
    #declare the var for maxDissarerance before obj can be marked as disapeared
    self.maxDisappeared = maxDisappeared

  #obj recoginition function
  def recoginition(self,centroid):
    #next available obj ID needs to be used when assiging 
    self.objects[self.nextObjectID] = centroid
    self.disappeared[self.nextObjectID] = 0
    self.nextObjectID += 1 

  # deregister funtion
  def deregister(self,objectID):
    # ID's need to be deleted from both dicts
    del self.objects[objectID]
    del self.objects[objectID]

  #updating obj ID if centroid (x,y) have moved
  def update(self,rects):
    # checking list of input boundaries (x,y) rectangle
    if len(rects) == 0:
      #go through exisiting ID's and mark any as disapeared if necesary
      for objectID in list(self.dissapeared.keys()):
        self.disappeared[objectID] += 1
        #if an obj has been missing for x number of times then mark as disapeared   
        if self.disappeared[objectID] > self.maxDisappeared:
          self.deregister(objectID)
      return self.objects

    #array containg input centroids for current frame
    inputCentroids = np.zeros((len(rects),2), dtype = 'int')
    #calculating centroid from bounding box 
    for (i, (startX,endX,startY,endY)) in enumerate(rect):
      # start + end / 2 to find the center coordinates for centroid
      cX = int((startX + endX) / 2.0 )
      cY = int((startY + endY) / 2.0 )
      inputCentroid[i] = (cX,cY)

    #if no objs are being tracked then take centroid as input and reg
    if len(self.objects) == 0:
      for i in range (0,len(inputCentroids)):
        self.regitser(inputCentroids[i])
    #else the obj is being tracked and the ID needs to be traced to the obj
    # centroid input and ID pair
    else:
      objectID = list(self.objects.keys())
      objectCentroids = list(self.objects.values)
      #calc distance between centroid obj pairs 
      D = dist.cdist(np.array(objectCentoirds),inputCentroid)
      # matchmaking smallest value in each row of input centroid and ID
      #sort the row < 
      rows = D.min(axis=1).argsort()
      #repeat process for cols 
      cols = D.argmin(axis = 1)[rows]
      #tracking which col & row indexs have been checked by update func 
      usedRow = []
      usedCol = []
      #loop tuple combinations of col & row index 
      for (row , col) in zip(rows,cols):
        #ignoring checked indexs
        if row in usedRow or col in usedCol:
          continue
        #if distance between 2 centroids is > than maxDist do not match with the same obj
        if D[row,col] > self.maxDistance:
          continue
        #find the obj ID for current row and set its new pos centroid 
        # reset dissapeared counter
        objectID = objectIDs[row]
        self.objects[objectID] = inputCentroids[col]
        self.dissapeared[objectID] = 0
        #indicate that all rows and cols have been eximined 
        usedRows.add(row)
        usedCols.add(col)
      #store the unchecked row & col index 
      unusedRow = set(range(0,D.shape[0])).difference(usedRows)
      unusedCol = set(range(0,D.shape[1])).difference(usedCols)
      #checking if the no. centroids input => obj centroids
      if D.shape[0] > D.shape[1]:
        #loop through unused row index
        for row in unusedRow:
          #get objID corresponding to the row
          objectID = objectIDs[row]
          self.disappeared[objectID] += 1 
          #check if that obj needs to be deregistered
          if self.dissapeared > maxDistance:
            self.deregister[objectID]
      #else the number of input centroids are > then new objects need to be reg
      else: 
        for col in unusedCols:
          self.regitser(inputCentroids[col])


  #return the tracked obj with boundries and centroids
    return self.objects

# trackable obj class 
class trackableObj:
  def __init__(self,objectID,centroid):
    #store and list of objID's
    self.objectID = objectID 
    self.centroid = [centroid]
    #init boolean inicator if obj has been counted
    self.counted = False
