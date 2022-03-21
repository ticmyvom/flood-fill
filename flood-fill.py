MAXCOLORVALUE = 2**16 - 1

class Solution:
    def tryAccessing(self, image, r, c):
        """
        :type image: List[List[int]]
        :type r: int
        :type c: int
        :rtype: int
        """
        try:
            a = image[r][c]
        except IndexError:
            return -1       # legit color value will be from 0 to 2^16 - 1
        else:
            return a

    def getNearbyNodesCoord(self, image, r, c):
        """
        :type image: List[List[int]]
        :type r: int
        :type c: int
        :rtype: ListList
        """
        nearbyNodes = list()
        if r - 1 >= 0: 
            nearby = self.tryAccessing(image, r-1, c)
            if nearby >= 0: nearbyNodes.append([r-1, c]) 
        if c - 1 >= 0: 
            nearby = self.tryAccessing(image, r, c-1)
            if nearby >= 0: nearbyNodes.append([r, c-1])

        if self.tryAccessing(image, r+1, c) >= 0:
            nearbyNodes.append([r+1, c])
        if self.tryAccessing(image, r, c+1) >= 0:
            nearbyNodes.append([r, c+1])
 
        return nearbyNodes

    # done via BFS
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        seen = list()
        queue1 = list()

        queue1.append([sr, sc])
        seen.append([sr, sc])

        while len(queue1) != 0:
            pixel = queue1.pop(0)
            r, c = pixel[0], pixel[1]

            # Processing step
            if image[r][c] == oldColor:
                image[r][c] = newColor

            # Handling nearby (4-directional) nodes
            neighbors = self.getNearbyNodesCoord(image, r, c)

            if len(neighbors) != 0:
                for coord in neighbors:
                    coordR = coord[0]
                    coordC = coord[1]

                    # append coord if not seen and it's the old color
                    if coord not in seen and image[coordR][coordC] == oldColor:
                        queue1.append(coord)
                        seen.append(coord)
        return image
        

      

listlist = [[1,1,1],[0,1,0],[1,0,155]]
# listlist = [[1,2,7],[10,111,90],[8,0,155]]
sr = 0
sc = 2
newColor = 2

sol = Solution()
print(sol.floodFill(listlist,sr,sc,newColor))

# nearby_nodes = sol.getNearbyNodesCoord(listlist, 2, 0)
# print(nearby_nodes)


