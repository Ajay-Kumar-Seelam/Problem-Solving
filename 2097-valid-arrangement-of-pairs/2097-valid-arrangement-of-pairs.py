class Solution:
    def validArrangement(self, pairs):
        adjacencyMatrix = collections.defaultdict(list)
        inDegree, outDegree = collections.defaultdict(
            int
        ), collections.defaultdict(int)


        for pair in pairs:
            start, end = pair[0], pair[1]
            adjacencyMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        result = []

        
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        
        if startNode == -1:
            startNode = pairs[0][0]

        nodeStack = [startNode]

        # Iterative DFS using stack
        while nodeStack:
            node = nodeStack[-1]
            if adjacencyMatrix[node]:
                # Visit the next node
                nextNode = adjacencyMatrix[node].pop(0)
                nodeStack.append(nextNode)
            else:
                # No more neighbors to visit, add node to result
                result.append(node)
                nodeStack.pop()

        result.reverse()

        
        pairedResult = []
        for i in range(1, len(result)):
            pairedResult.append([result[i - 1], result[i]])

        return pairedResult