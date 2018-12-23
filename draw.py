#!/usr/bin/python

import sys, os, os.path, re, time, datetime, locale, requests, random
import pandas as pd
import numpy as np


draw = []
n1 = random.randrange(1, 20)
n2 = random.randrange(5, 25)
n3 = random.randrange(15, 35)
n4 = random.randrange(25, 45)
n5 = random.randrange(35, 50)
n6 = random.randrange(45, 60)
    
draw.extend([n1, n2, n3, n4, n5, n6])

print (draw)
