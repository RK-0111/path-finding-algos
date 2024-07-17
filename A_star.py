graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2, 5],
    5: [2, 6],
    6: [3, 4]
}
def heuristic(node, goal):
    heuristic_values = {
        1: 4,
        2: 3,
        3: 2,
        4: 2,
        5: 1,
        6: 0
    }
    return heuristic_values.get(node,0)
def A_STAR(graph,start,end,heuristic):
    queue=[(heuristic(start,end),start)]
    done=[]
    cost={start:0}
    prev={}
    while queue:
        queue.sort()
        current_cost,current_node=queue.pop(0)
        if current_node==end:
            path=[]
            while current_node!=start:
                path.append(current_node)
                current_node = prev[current_node]
            path.append(start)
            path.reverse()
            return path
        done.append(current_node)
        for x in graph[current_node]:
            if x not in done:
                new_cost = cost[current_node] + 1
                if x not in cost or new_cost < cost[x]:
                    cost[x] = new_cost
                    priority = new_cost + heuristic(x, end)
                    queue.append((priority,x))
                    prev[x] = current_node
start=1
end=6
path=A_STAR(graph,start,end,heuristic)
print(f"Path found from {start} to {end}: {path}")


