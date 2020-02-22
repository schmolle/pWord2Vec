import numpy
import numpy.linalg

def cosSim(vec1,vec2):
    return numpy.dot(vec1, vec2) / (numpy.linalg.norm(vec1) * numpy.linalg.norm(vec2))