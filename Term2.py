import numpy as np
from math import *

def euclidian_dist(p1, p2):
    diff = p1 - p2
    diff2 = diff**2
    m=np.sum(diff2)
    ed=np.sqrt(m)
    #ed=np.sqrt(np.sum(p1-p2)**2)
    return ed

p1 = np.array([0,2])
p2 = np.array([2,0])
b = euclidian_dist(p1, p2)
print("Eucledian distance between p1 and p2 is : ", b)

def jaccard_binary(x, y):
    """A function to find similarity between two binary vectors"""
    intersection = np.logical_and(x,y)
    #print(intersection)
    union = np.logical_or(x,y)
    #print(union)
    similarity = intersection.sum() / float(union.sum())
    return similarity

x = [0,1,1,1]
y = [1,0,1,1]
simxy=jaccard_binary(x,y)
print("jaccard Similarity between x and y is ",simxy)

def square_rooted(x1):
    return round(sqrt(sum([a*a for a in x1])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
    
x = cosine_similarity([3,2,0,5,0,0,0,2,0,0],[1,0,0,0,0,0,0,1,0,2])
print("Cosine Similarity between x and y is ",x)