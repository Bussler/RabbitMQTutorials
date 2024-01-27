# Chapter 2
- Declare task queues that give incoming messenges to workers in a round-robin fashion.
- `new_task.py`: Sender, puts messenges into queue. (Get messenge from command line argument)
- `worker.py`: Receiver, gets messenges from queue and prints it. (After waiting some amount)