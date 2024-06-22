import collections
def bfs(graph,visited,node):
    queue = collections.deque([node])
    visited.add(node)
    while graph is not None:
        node=queue.pop()
        print(node)
        for i in graph[node]:
            if i is not visited:
                visited.add(i)
                queue.appendleft(i)
visited=set()
graph={
    'A':['B','C','D'],
    'B':['E'],
    'C':['E','F'],
    'D':['F'],
    'E':['G'],
    'F':['G'],
    'G':[],
}
bfs(graph,visited,'A')

