from collections import deque

def DFS(graph):
    visited = [0]*len(graph)  # element visited array (0 = not visited)(1 = visited)
    stack = []  # stack for DFS
    search = []  # for searching path 
    visited[0] = 1   # starting from 0 element 
    stack.append(0)
    for j in range(0,len(graph)):
        ele = stack.pop()    # poping top element from stack
        search.append(ele)
        for i in graph[ele]:
            if(visited[i]==0):     # if element is not visited then we append in stack and mark as visited
                stack.append(i)
                visited[i]=1
    return search

def BFS(graph):
    visited = [0]*len(graph)
    queue = deque()  # queue for BFS
    search = []
    visited[0] = 1       # starting from 0 element
    queue.append(0)
    for j in range(0,len(graph)):
        ele = queue.popleft()   # poping front element from deque
        search.append(ele)
        for i in graph[ele]:
            if(visited[i]==0):  # if element is not visited then we append in queue and mark as visited
                queue.append(i)
                visited[i]=1
    return search


graph = {
    0:[1,3,6],
    1:[0,2,5,6],
    2:[1,3,4,5],
    3:[0,2,5],
    4:[2],
    5:[1,2,3],
    6:[0,1]
}

print(graph)
print(f"DFS : {DFS(graph=graph)}")
print(f"BFS : {BFS(graph=graph)}")