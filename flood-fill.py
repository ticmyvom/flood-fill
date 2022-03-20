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
            return -1
        else:
            return a

    def getNearbyNodesWCoordinates(self, image, r, c):
        """
        :type image: List[List[int]]
        :type r: int
        :type c: int
        :rtype: Dict of 0:List and 1:ListList
        """
        nearbyNodes = list()
        nodesCoord = list()
        # possiblePlace = 
        # return a list of all nearby 4 directional nodes; value = -1 if there is IndexError
        if r - 1 >= 0:
            nearbyNodes.append(self.tryAccessing(image, r-1, c))
        else: nearbyNodes.append(-1)
        nodesCoord.append([r-1, c]) 
        if c - 1 >= 0:
            nearbyNodes.append(self.tryAccessing(image, r, c-1))
        else: nearbyNodes.append(-1) 
        nodesCoord.append([r, c-1])

        nearbyNodes.append(self.tryAccessing(image, r+1, c))
        nodesCoord.append([r+1, c]) 
        nearbyNodes.append(self.tryAccessing(image, r, c+1)) 
        nodesCoord.append([r, c+1])
        
        return {0:nearbyNodes, 1:nodesCoord}
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        print("Hi")
        print(image[2][2])

      

# listlist = [[1,1,1],[0,1,0],[1,0,155]]
listlist = [[1,2,7],[10,111,90],[8,0,155]]
sr = 0  
sc = 2
newColor = 2

sol = Solution()
sol.floodFill(listlist,sr,sc,newColor)

# dict1 = sol.getNearbyNodesWCoordinates(listlist, 2, 1)
# nearby_nodes = dict1[0]
# nodes_coord = dict1[1]
# print(nearby_nodes)
# print(nodes_coord)