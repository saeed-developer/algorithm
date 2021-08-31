edjes = [
['a','b'],
['c','a'],
['d','c'],
['c','e'],
['f','g']
]
#this function get list of edges and create a graph with them
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
#this algorithm check if there is a path in the cycle graph with depth-first algorithm
def hasPath(edjes,start,des):
   graph = buildGraph(edjes)
   visited = set()
   stack = [start]
   visited.add(start)
   while len(stack) > 0:
       current = stack.pop()
       if current == des:
           return True
       for y in graph[current]:
           if y not in visited:
            visited.add(y)
            stack.append(y)
   return False