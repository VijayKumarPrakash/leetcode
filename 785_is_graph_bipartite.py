import itertools
from collections import deque

class Solution:
    def getOther(self, color):
        if color == 'red':
            return 'blue'
        return 'red'

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color_map = {}
        visited = set()

        for i in range(len(graph)):
            if i not in visited:
                q = deque([i])
                visited.add(i)
                color_map[i] = 'red'
                while q:
                    current = q.popleft()
                    for neighbour in graph[current]:
                        if neighbour not in color_map:
                            color_map[neighbour] = self.getOther(color_map[current])
                            visited.add(neighbour)
                            q.append(neighbour)
                        elif color_map[neighbour] == color_map[current]:
                            return False

        return True

    # def isBipartite(self, graph: List[List[int]]) -> bool:
    #     left = set([0])
    #     right = set()

    #     for i in range(len(graph)):
    #         row = graph[i]
    #         if not row:
    #             continue
            
    #         for m,n in itertools.combinations(row, 2):
    #             if n in graph[m]:
    #                 return False
    #         if i in left or right.intersection(row):
    #             print(i, "goes in left and neighbours in right")
    #             right.update(row)
    #             left.update([i])
    #         elif i in right or left.intersection(row):
    #             print(i, "goes in right and neighbours in left")
    #             left.update(row)
    #             right.update([i])
    #         else:
    #             # left.update(row)
    #             # right.update([i])
    #             continue
    #         print("Left, right after", i)
    #         print(left)
    #         print(right)
        
    #     for i,j in itertools.combinations(left, 2):
    #         if j in graph[i]:
    #             return False
        
    #     for i,j in itertools.combinations(right, 2):
    #         if j in graph[i]:
    #             return False
        
    #     return True
