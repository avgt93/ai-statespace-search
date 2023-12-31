from enum import Enum

class Action:
  def __init__(self, value: int):
    self.value: int = value
  def __str__(self) -> str:
    if self == Action_Space.Up:
      return "Up"
    if self == Action_Space.Down:
      return "Down"
    if self == Action_Space.Left:
      return "Left"
    if self == Action_Space.Right:
      return "Right"

class Action_Space:
  Left: Action = Action(-1)
  Up: Action = Action(-3)
  Down: Action = Action(3)
  Right: Action = Action(1)

class Game_State(Enum):
  Running: int = 0
  Won: int = 1

class State:
  def __init__(self, numList: list):
    self.num_list: list = numList

  def __str__(self) -> str:
    temp: str = ""
    for i in range(0, len(self.num_list)):
      temp += str(self.num_list[i])
      if (i + 1) % 3 == 0:
        temp += "\n"
    return temp

class Game:
  game_status: Game_State = Game_State.Running
  move_performed: Action = None

  def __init__(self, current_state: State, goal_state: State):
    self.current_state: State = current_state
    self.goal_state: State = goal_state

  def __str__(self) -> str:
    temp: str = f"Current State:\n{self.current_state}"
    return temp

  def check_game(self) -> None:
    if self.current_state.num_list == self.goal_state.num_list:
      self.game_status = Game_State.Won

  def move(self, action: Action) -> bool:
    blank_index: int = self.current_state.num_list.index(" ")
    if self.game_status != Game_State.Running:
      return False

    if action == Action_Space.Left:
      if (blank_index + 1) % 3 == 1:
        return False

    if action == Action_Space.Up:
      if blank_index < 3:
        return False

    if action == Action_Space.Down:
      if blank_index > 5:
        return False

    if action == Action_Space.Right:
      if (blank_index + 1) % 3 == 0:
        return False

    self.check_game()
    self.current_state.num_list[blank_index] ,self.current_state.num_list[blank_index+action.value] = self.current_state.num_list[blank_index + action.value], self.current_state.num_list[blank_index]
    self.move_performed = action
    self.check_game()
    return True


game: Game = Game(State([1, 2, 3, 4, 5, 6, 7, 8, " "]), State([1, 2, 3, 4, 5, 6, 7, 8, " "]))
print(game)
