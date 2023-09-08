from enum import Enum

class GameState(Enum):
  Running: int = 0
  Won: int = 1  
  
class Action:
  def __init__(self,value):
    self.value = value
    
  def __str__(self):
    if self == ActionSpace.MoveUp:
      return "Up"
    if self == ActionSpace.MoveDown:
      return "Down"
    if self == ActionSpace.MoveLeft:
      return "Left"
    if self == ActionSpace.MoveRight:
      return "Right"
    
    
class ActionSpace:
  MoveLeft: Action = Action(-1)
  MoveUp: Action = Action(-3)
  MoveDown: Action = Action(3)
  MoveRight: Action = Action(1)
  
class State:
  def __init__(self,numList:list):
    self.numList = numList
  def __str__(self):
      temp = ""
      for i in range(0, len(self.numList)):
          temp += str(self.numList[i])
          if (i + 1) % 3 == 0:
              temp += "\n"
      return temp

class Game:
  gameStatus:GameState = GameState.Running
  movePerformed: Action = None
  
  def __init__(self,current_state:State,goal_state:State):
    self.current_state = current_state
    self.goal_state = goal_state
    
  def __str__(self):
    temp =f"Current State:\n{self.current_state}"
    return temp
  
  def check_game(self):
     if self.current_state.numList == self.goal_state.numList:
       self.gameStatus = GameState.Won
       
  def move(self, action:Action):
    emptyPos =self.current_state.numList.index(" ")
    if self.gameStatus != GameState.Running:
      return False
    
    if action == ActionSpace.MoveLeft:
      if (emptyPos+1)%3 ==1:
        return False
      
    if action == ActionSpace.MoveUp:
          if emptyPos < 3:
              return False

    if action == ActionSpace.MoveDown:
        if emptyPos > 5:
            return False

    if action == ActionSpace.MoveRight:
        if (emptyPos + 1) % 3 == 0:
            return False
    
    self.current_state.numList[emptyPos]=self.current_state.numList[emptyPos + action.value]
    
    self.current_state.numList[emptyPos + action.value] = " "
    self.movePerformed = action
    self.check_game()
    return True
       
