import bsync

def coro1():
  print("Hello world")
  yield bsync.sleep(2)
  return 1

def coro2():
  print("My name is james")
  yield bsync.sleep(1)
  return 2

def main():
  t1 = bsync.create_task(coro1())
  t2 = bsync.create_task(coro2())
  t1.add_done_callback(lambda t: print("Task 1 done"))
  t2.add_done_callback(lambda t: print("Task 2 done"))
  res2 = yield bsync.wait(t2)
  res1 = yield bsync.wait(t1)
  print(f"Results: {res1}, {res2}")
bsync.run(main)
