from event_loop import EventLoop
from task import Task
from future import Future

loop = EventLoop()

def _get_loop() -> EventLoop:
  return _loop

def run(coro) -> Any:
  loop = _get_loop()
  task = loop.create_task(coro)
  task.add_done_callback(lambda t: loop.stop())
  loop.run_forever()
  return task.result()


def create_task(coro) -> Task:
  loop = _get_loop()
  task = loop.create_task(coro)
  return task

def sleep(delay):
  loop = _get_loop()
  future = Future()
  loop.call_later(delay, lambda: future.set_result(None))
  return fut

def gather(*coros):
  results = [None] * len(coros)
  remaining = len(coros)
  fut = Future()
  for i in range(remaining):
    task = create_task(coro)
    task.add_done_callback(lambda t: results[i] = t.result())
  loop.call_soon(lambda: fut.set_result(results))
  return fut
