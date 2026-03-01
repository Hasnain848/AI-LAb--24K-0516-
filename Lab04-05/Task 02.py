graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':['G'],
'E':[],
'F':['H'],
'G':[],
'H':[]
}
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
  def dls(self,graph,start,goal,depth_limit):
    visited=[]
    def dfs(node,depth,path):
      if depth>depth_limit:
        return None
      visited.append(node)
      path.append(node)
      if node==goal:
        return path.copy()
      for neighbor in graph.get(node,[]):
        if neighbor not in path:
          result=dfs(neighbor,depth+1,path)
          if result:
            return result
      path.pop()
      return None
    final_path=dfs(start,0,[])
    print("Depth Limit:",depth_limit)
    print("Visited Order:")
    print(visited)
    if final_path:
      print("Path to Goal:")
      print(final_path)
    else:
      print("No path found.")
    return final_path
  def Act(self,percept,graph,depth_limit):
    goal_status=self.formulate_goal(percept)
    if goal_status=="Goal Reached":
      return "Goal:"+self.goal+" Found!"
    else:
      return self.dls(graph,percept,self.goal,depth_limit)
#===============================================================================
def Run_Agent(enviroment,agent,start_node,depth_limit):
  percept=enviroment.get_percept(start_node)
  action=agent.Act(percept,enviroment.graph,depth_limit)
  #print(action)
#===============================================================================
start_node='A'
goal_node='H'
enviroment=Enviroment(graph)
agent=Goal_Based_Agent(goal_node)
Run_Agent(enviroment,agent,start_node,2)
print()
Run_Agent(enviroment,agent,start_node,3)
