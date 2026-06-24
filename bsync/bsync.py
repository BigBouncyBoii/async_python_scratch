from event_loop import EventLoop

class Bsync:
  
  def __init__(self):
    self.loop = event_loop.EventLoop()
  
  def get_event_loop() -> "EventLoop":
    return self.loop
  
  

