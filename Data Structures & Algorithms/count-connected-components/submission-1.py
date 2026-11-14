class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #maintain a set called visited
        visited = set()
        #construct an adj list for edges
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0
        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)

        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count
        