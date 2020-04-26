'''
graph = {
    "1": ["3"],
    "2": ["3", "4"],
    "3": ["1", "2", "4"],
    "4": ["2", "3", "5"],
    "5": ["4", "6", "7"],
    "6": ["5"],
    "7": ["5"]
}
graph2 = {
    "11": ["3"],
    "2": ["3", "42"],
    "3": ["11", "2", "42"],
    "42": ["2", "3", "54"],
    "54": ["42", "6", "71"],
    "6": ["54"],
    "71": ["54"]
}

a = {'a': 1}
b = {'b': 2}
c = {'c': 3}
d = {'d': 4}

gg = {
    'a': [],
    'b': ['a', 'd'],
    'd': ['c'],
    'c': []
}
# Set to keep track of visited nodes.
'''


def deep_find(data, key):
    if key in data:
        return data[key]
    for k, v in data.items():
        if isinstance(v, dict):
            result = deep_find(v, key)
            if result is not None:
                return result


def deep_find_all(data, key, found=None):
    if found is None:
        found = list()

    if key in data:
        found.append(data[key])

    for k, v in data.items():
        if isinstance(v, dict):
            result = deep_find_all(v, key, found)
            if result is not None:
                return result
    return found


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


def bfs(graph, node, visited=None):
    if visited is None:
        visited = []
        queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def deep_update(data, key, val):
    if key in data:
        data[key] = val

    for k, v in data.items():
        if isinstance(v, dict):
            deep_update(v, key, val)

    return data


def deep_compare(obj1, obj2):
    for k, v in obj1.items():
        if k not in obj2:
            return False
        else:
            if isinstance(v, dict):
                return deep_compare(v, obj2[k])
            else:
                if v != obj2[k]:
                    return False

    return True
