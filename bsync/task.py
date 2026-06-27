
from future import Future
from typing import Any, Callable

class Task:
  def __init__(self, coro: Callable, loop: EventLoop):
    self.loop = loop
    self.coro = coro
    self.callbacks = []
    self._done = False
    self._result = None
  
  def step(self, value = None):
    try:
      res = self.coro.send(value)
      if isinstance(res, Future):
        res.add_done_callback(self._wakeup)
        return
      elif isinstance(res, Task):
        if res.done():
          self.loop.call_soon(self.step, res.result())
        else:
          res.add_done_callback(self._wakeup)
        return
    except StopIteration as e:
      self._done = True
      self._result = e.value
      for cb in self.callbacks:
        cb(self)

  def done(self) -> bool:
    return self._done
  
  def result(self) -> Any:
    return self._result
  
  def add_done_callback(self, cb: Callable):
    if self.done():
      cb(self)
    else:
      self.callbacks.append(cb)
  
  def _wakeup(self, future: Future):
    self.loop.call_soon(self.step, future.get_result())
