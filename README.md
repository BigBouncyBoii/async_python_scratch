# async_python_scratch

Creating asyncio library from scratch to understand how it works under the hood. 

Called bsync since my user name is bigbouncyboii

Lifecycle of a task

create_task
   ↓
schedule task.step
   ↓
run step
   ↓
hit await → return Future
   ↓
pause task
   ↓
Future completes
   ↓
schedule task.step again
   ↓
repeat
