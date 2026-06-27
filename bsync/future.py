from enum import Enum
from typing import List, Any, Callable
import event_loop

class Status(Enum):
  PENDING = "Pending"
  FINISHED = "Finished"

class Future:
  def __init__(self):
    self.status: Status = Status.PENDING
    self.result: Any = None
    self.callbacks: List[Callable] = []
  
  def done(self) -> bool:
    return self.status == Status.FINISHED
  
  def get_result(self) -> Any:
    return self.result

  def set_result(self, result: Any):
    if self.done():
      return
    else:
      self.result = result
      self.status = Status.FINISHED
      for cb in self.callbacks:
        cb(self)

  def add_done_callback(self, cb: Callable):
    if self.done():
      cb(self)
    else:
      self.callbacks.append(cb)
