def dfs(graph,visited,node):
    if node  not in  visited:
        print(node)
        visited.add(node)
        for adj in graph[node]:
            if adj is not visited:
                dfs(graph,visited,adj)
visited=set()
graph={
         1:[2,3],
        2:[1,4],
        3:[1,4],
        4:[2,3],
        # Add more nodes and edges as needed
    }
dfs(graph,visited,1)
