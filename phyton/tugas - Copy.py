jalur = {'A': (['B ','C']),
        'B': (['A','D','E']),
        'D': (['B','H']),
        'E': (['B','H']),
        'H': (['D','E','J']),
        'C': (['A','F','G']),
        'F': (['I','C']),
        'G': (['I','C']),
        'I': (['F','G','J']),
        'J': (['I','H'])
}

def prosess(jalur, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for node in jalur[start]:
        if node not in path:
            new_path = prosess(jalur, node, goal, path + [node])
            if new_path is not None:
                return new_path

start_node = 'A'
goal_node = 'J'

path = prosess(jalur, start_node, goal_node)
print (path)
