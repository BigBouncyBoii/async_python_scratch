from collections import deque
import heapq
import time

class EventLoop:
  
  def __init__(self):
    self._ready = deque() 
    self._timers = []
    self._running = False
  
  def call_soon(self, callback):
    self._ready.append(callback)

  def call_later(self, delay, callback):
    curr = time.time()
    heapq.heappush(self._timers, (curr+delay, callback))

  def create_task(self, coro):
    task = Task(coro, self)
    self._ready.append(task.step)
    return task

  def run_forever(self):
    self._running = True
    while self._running:
      self._run_timers()
      self._run_ready()
      self._idle_sleep()

  def stop(self):
    self._running = False
  
  def _run_ready(self):
    while len(self._ready) > 0:
      cb = self._ready.popleft()
      cb()
  
  def _run_timers(self):
    current = time.time()
    while len(self._timers) > 0:
      time, cb = self.timers[0]
      if current > time:
        break
      heapq.heappop(self._timers)
      self._ready.append(cb)
  
  def _idle_sleep(self):
    time.sleep(1)
