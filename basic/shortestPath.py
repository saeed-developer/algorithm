edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
def buildGraph(edjes):
   graph = {}
   for x in edjes:
      item1 = x[0]
      item2 = x[1]
      if item1 not in graph:
          graph[item1] = []
      if item2 not in graph:
          graph[item2] = []
      graph[item1].append(item2)
      graph[item2].append(item1)
   return graph


def shortestPath(edges, start,des):
  graph = buildGraph(edges)
  visited = set()
  queue = [[start,0]]
  while len(queue) > 0:
       current = queue[0][0]
       distance  = queue[0][1]
       queue.pop(0)
       if current == des:
         return distance
       for y in graph[current]:
           if y not in visited:
             visited.add(y)
             queue.append([y , distance + 1])
  return -1
