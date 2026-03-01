tree={
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
  def dls(self,graph,node,goal,depth,path):
    if depth==0:
      return False
    if node==goal:
      path.append(node)
      return True
    if node not in graph:
      return False
    for child in graph[node]:
      if self.dls(graph,child,goal,depth-1,path):
        path.append(node)
        return True
    return False
  def iterative_deepening(self,graph,start,goal,max_depth):
    for depth in range(max_depth+1):
      print("Depth:",depth)
      path=[]
      if self.dls(graph,start,goal,depth,path):
        print("Path to goal:"," → ".join(reversed(path)))
        return
    print("Goal not found within depth limit.")
  def Act(self,percept,graph,depth):
    goal_status=self.formulate_goal(percept)
    if goal_status=="Goal Reached":
      return "Goal:"+self.goal+" Found!"
    else:
      return self.iterative_deepening(graph,percept,self.goal,depth)
#===============================================================================
def Run_Agent(enviroment,agent,start_node,depth_limit):
  percept=enviroment.get_percept(start_node)
  action=agent.Act(percept,enviroment.graph,depth_limit)
  return action
#===============================================================================
start_node='A'
goal_node='G'
enviroment=Enviroment(tree)
agent=Goal_Based_Agent(goal_node)
Run_Agent(enviroment,agent,start_node,4)
