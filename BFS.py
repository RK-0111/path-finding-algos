graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2, 5],
    5: [2, 6],
    6: [3, 4]
}
done=[]
def BFS(done,graph,s_node):
    queue=[s_node]
    while queue:
        node=queue.pop(0)
        if node not in done:
            print(node)
            done.append(node)
            for x in graph[node]:
                if x not in done:
                    queue.append(x)
BFS(done,graph,1)


