graph = {
'S': {'A': 4, 'B': 2},
'A': {'C': 5, 'D': 10},
'B': {'E': 3},
'C': {'G': 4},
'D': {'G': 1},
'E': {'D': 4},
'G': {}
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
  def ucs(self,graph,start,goal):
    frontier=[(start,0)]
    visited=set()
    came_from={start:None}
    cost_so_far={start:0}
    while frontier:
      frontier.sort(key=lambda x:x[1])
      current_node,current_cost=frontier.pop(0)
      if current_node in visited:
        continue
      visited.add(current_node)
      print("Visiting:",current_node,"Cost so far:",current_cost)
      if current_node==goal:
        path=[]
        while current_node is not None:
          path.append(current_node)
          current_node=came_from[current_node]
        path.reverse()
        print("Goal found with UCS. Path:",path,"Total Cost:",current_cost)
        return path,current_cost
      for neighbor,cost in graph[current_node].items():
        new_cost=current_cost+cost
        if neighbor not in cost_so_far or new_cost<cost_so_far[neighbor]:
          cost_so_far[neighbor]=new_cost
          came_from[neighbor]=current_node
          frontier.append((neighbor,new_cost))
    print("Goal not found")
    return None,None
  def Act(self,percept,graph):
    goal_status=self.formulate_goal(percept)
    if goal_status=="Goal Reached":
      return "Goal:"+self.goal+" Found!"
    else:
      return self.ucs(graph,percept,self.goal)
#===============================================================================
def Run_Agent(enviroment,agent,start_node):
  percept=enviroment.get_percept(start_node)
  action=agent.Act(percept,enviroment.graph)
  return action
#===============================================================================
start_node='S'
goal_node='G'
enviroment=Enviroment(graph)
agent=Goal_Based_Agent(goal_node)
Run_Agent(enviroment,agent,start_node)
