Building = [
[1, 1, 0, 1],
[0, 1, 1, 1],
[1, 1, 0, 1],
[1, 0, 1, 1]
]
directions = [(0,1),(0,-1),(1,0),(-1,0)]
#===============================================================================
def create_garph(Building):
  graph={}
  rows=len(Building)
  cols=len(Building[0])
  for i in range(rows):
    for j in range(cols):
      if Building[i][j]==1:
        neighbours=[]
        for dx,dy in directions:
          nx,ny=dx+i,dy+j
          if 0<=nx<rows and  0<=ny<cols and Building[nx][ny]==1:
            neighbours.append((nx,ny))
        graph[(i,j)]=neighbours
  return graph
#===============================================================================
class Enviroment:
  def __init__(self,graph):
    self.graph=graph
  def get_percept(self,node):
    return node
#===============================================================================
class Goal_Based_Agent:
  def __init__(self,goal):
    self.goal=goal
  def formulate_goal(self,percept):
    if percept==self.goal:
      return "Goal Reached"
    return "Searching"
  def bfs_search(self,graph,start,goal):
    visited=[]
    queue=[]
    parent = {}
    visited.append(start)
    queue.append(start)
    parent[start]=None
    print("Traversal Order: ")
    while queue:
      node=queue.pop(0)
      print(f"->Visiting: {node}")
      if node == goal:
        path=[]
        while node is not None:
          path.append(node)
          node=parent[node]
        path.reverse()
        print("\nShortest Path:")
        for p in path:
          print(p, end=" -> ")

          print("END")     
        return f"Goal Found!";
      for neighbour in graph[node]:
        if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)
          parent[neighbour] = node
    return "Goal not Found"
  
  def Act(self,percept,graph):
    goal_status=self.formulate_goal(percept)
    if goal_status=="Goal Reached":
      return  f"Goal:{self.goal} Found!";
    else:
      return self.bfs_search(graph,percept,self.goal)
#===============================================================================
def Run_Agent(enviroment,agent,start_node):
  percept=enviroment.get_percept(start_node)
  action=agent.Act(percept,enviroment.graph)
  return action
#===============================================================================
start_node=(0,0)
goal_node=(3,3)
enviroment=Enviroment(create_garph(Building))
agent=Goal_Based_Agent(goal_node)
Run_Agent(enviroment,agent,start_node)

