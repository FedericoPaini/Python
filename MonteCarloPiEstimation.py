#!/usr/bin/python

import random

totalPoints = 10000000 # Total points inside the square
pointsInside  = 0 # Points inside the circle


for points in xrange(0,totalPoints):
	x = (random.random() * 2 - 1)
	y = (random.random() * 2 - 1)

	if (x * x) + (y * y) <= 1 : #If a point is inside the circle then the distance between the point and the center of the circle (0, 0) will be at most 1.
		pointsInside += 1
		#print pointsInside

pi = 4.0 * (float(pointsInside) / float(totalPoints)) # pi estimation since the ratio AreaSquare/AreaCircle = pi/4
print pi