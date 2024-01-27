# Chapter 4
- Subscribe to only a subset of messenges with direct exchanger.
- `sender.py`: Sender, puts messenges to exchanger. (Get messenge from command line argument)
- `worker.py`: Receiver, creates new temporary custom queues. Subscribes queue to routing key. Gets messenges from queue and prints it.
