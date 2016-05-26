__author__ = 'Ryan Cabrera'

graph = {'A': [('B', 1), 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print(graph)

for node in graph:
    print(node, graph.get(node))
