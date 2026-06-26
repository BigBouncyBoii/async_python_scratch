
from future import Future
from typing import Any

class Task:
  def __init__(self, coro, loop):
    self.loop = loop
    self.coro = coro
  
  def step(self, value = None):
    future = self.coro.send(value)
    if isinstance(future, Future):
      future.add_done_callback(self._wakeup)
  
  def done(self) -> bool:
    pass
  
  def result(self) -> Any:
    pass
  
  def add_done_callback(self):
    pass
  
  def _wakeup(self, future):
    self.loop.call_soon(self.step, future.get_result())
