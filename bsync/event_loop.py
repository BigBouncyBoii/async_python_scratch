from collections import deque
import heapq
import time

class EventLoop:
  
  def __init__(self):
    self._ready = deque() 
    self._timers = []
    self._running = False
  
  def call_soon(self, callback, *args):
    self._ready.append((callback, args))

  def call_later(self, delay, callback, *args):
    curr = time.time()
    heapq.heappush(self._timers, (curr+delay, callback, args))

  def create_task(self, coro):
    task = Task(coro, self)
    self._ready.append((task.step, ())) #this is a function task.step 
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
      cb, args = self._ready.popleft()
      cb(*args)
  
  def _run_timers(self):
    current = time.time()
    while len(self._timers) > 0:
      run_at, cb, args = self._timers[0]
      if current < run_at:
        break
      heapq.heappop(self._timers)
      self._ready.append((cb, args))
  
  def _idle_sleep(self):
    time.sleep(1)
