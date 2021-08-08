# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def containsPoint(segment,point):
    return segment.start <= point and segment.end >= point

def getSegmentsContainPoint(segments,point):
    return list(filter(lambda s: not containsPoint(s,point),segments))

def optimal_points(segments):
    points = []
    maxPoints = 0
    segments.sort(key=lambda x: x.end)
    while len(segments)>0:
        s = segments[0]
        segments = getSegmentsContainPoint(segments,s.end)
        points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
