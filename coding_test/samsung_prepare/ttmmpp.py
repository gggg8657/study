def sprint(arr):
    for _ in range(len(arr)):
        print(arr[_])
    print("* * * * * * * * *")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Step 1: Transpose the matrix
transposed = list(zip(*matrix))
print(transposed)
# Step 2: Reverse each row
rotated_matrix = [list(row[::-1]) for row in transposed]

# Print the rotated matrix
for row in rotated_matrix:
    print(row)

print("\n\n\n")
narr = [x[:] for x in rotated_matrix]

lol = map(lambda x: int(x) -1, input().split())

sprint(narr)
for row in range(len(rotated_matrix)):
    for col in range(len(rotated_matrix)):
        narr[row][col] = rotated_matrix[len(rotated_matrix)-col-1][row]

sprint(narr)
sprint(rotated_matrix)


def dfs(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()

    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()

        ##만약 방문한 리스트에 없다면
        if node not in visited:
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited


def dfs_recursive(graph, start, visited=[]):
    ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited


def dfs_rec(adj, visited, s):
    # Mark the current vertex as visited
    visited[s] = True

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_rec(adj, visited, s)


def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)


if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)


def get_combinations_recursive(arr, r):
    def combine(current, start):
        if len(current) == r:
            result.append(current[:])
            return

        for i in range(start, len(arr)):
            current.append(arr[i])
            combine(current, i + 1)
            current.pop()

    result = []
    combine([], 0)
    return result


# 사용 예시
arr = [1, 2, 3, 4]
r = 2
print(get_combinations_recursive(arr, r))

def make_snake(arr):