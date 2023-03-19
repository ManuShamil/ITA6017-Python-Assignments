# Given 'n' points, design a flowchart or an algorithm and write the Python code to determine the pair
# of points that are far from each other. Distance between two points (x1, y1)
# and (x2, y2) is determined using the formula

import math


# function for calculating the distance between two point
def distance_between_two_point(point1, point2):
    return round(math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2), 2)


# calculatin which two point will have max distance
def max_distance(points):

    # initially the points will be None(null)
    p1 = None
    p2 = None

    max_distance = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            curr_distance = distance_between_two_point(points[i], points[j])
            if curr_distance > max_distance:
                max_distance = curr_distance
                p1 = points[i]
                p2 = points[j]
    return p1, p2, max_distance


if __name__ == '__main__':
    points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    p1, p2, max_distance = max_distance(points)
    print(f"The points which are far from each other is  {p1} and {p2} with a distance of {max_distance}")
