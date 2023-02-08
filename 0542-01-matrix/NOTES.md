brute force solution explanation:
initialize answer matrix to be an impossibly large value.
for each cell in the original matrix
first we check if the cell is equal to 0 and if so, we set that cell to 0, if not, we look at each cell in the matrix and compute the smallest distance from that cell to the cell we are looking at if the cell is 0.
Essentially we are finding all the zeros, and calculating distances to the 0.
The key takeaway here is the distance function `abs(k - i) + abs(l - j)`
​
breadth first search;
replace the brute force search (the deepest nested for loop) with breadth first search.
​
Here, we fill a queue with where all the 0s are, and then for each item in the queue, we fill the adjacent cells that we havent looked at (marked by r\*c) with 1 plus the place we were looking in, and then we add that location to the queue. We keep going until we have seen every nonzero cell. (how can we guarantee that we see everything)