graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2, 5],
    5: [2, 6],
    6: [3, 4]
}
done=[]
def DFS(done,graph,node):
    if node not in done:
        print(node)
        done.append(node)
        for x in graph[node]:
            DFS(done,graph,x)
DFS(done, graph, 1)