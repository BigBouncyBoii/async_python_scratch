import bsync

def task1():
  print("Hello world")
  bsync.sleep(1)

def task2():
  print("My name is james")
  bsync.sleep(2)

def main():
  t1 = bsync.create_task(task1)
  t2 = bsync.create_task(task1)

bsync.run(main)
