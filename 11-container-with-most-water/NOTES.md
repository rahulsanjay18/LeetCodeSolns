The logic here is to understand a few things off the bat:

area = width * height

where width is the distance between the index of the first wall and the index of the second wall. 

height is the minimum height between the two walls. 

keeping the max area for every thing tried is trivial. Start by testing the area at both ends of the array, because we assume that the largest width will give us the max area, and because we only need to move in one direction on either side to test each next area. We choose the next area to test by picking the lowest wall and trying the one next to it, hoping that this wall is higher and will result in a larger area, compensating for the reduction in width.
