from enum import Enum

class Status(Enum):
  PENDING = "Pending"
  FINISHED = "Finished"
  CANCELLED = "Cancelled"

class Future:
  def __init__(self):
    self.status: Status = Status.PENDING
    self.result: Any = ""
  
  def set_result(self, result):
    self.result = result
    self.status = Status.FINISHED
    
