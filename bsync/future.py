from enum import Enum
from typing import List, Any, Callable
import event_loop

class Status(Enum):
  PENDING = "Pending"
  FINISHED = "Finished"

class Future:
  def __init__(self, loop):
    self.loop: EventLoop = loop
    self.status: Status = Status.PENDING
    self.result: Any = None
    self.callbacks: List[Callable] = []
  
  def _done(self):
    return self.status == Status.FINISHED
  
  def get_result(self) -> Any:
    return self.result

  def set_result(self, result) -> void:
    if self._done():
      return
    else:
      self.result = result
      self.status = Status.FINISHED
      for cb in self.callbacks:
        self.loop.call_soon(cb, self)

  def add_done_callback(self, cb) -> void:
    if self._done():
      self.loop.call_soon(cb, self)
    else:
      self.callbacks.append(cb)
