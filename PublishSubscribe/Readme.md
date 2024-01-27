# Chapter 3
- Declare exchanges for queues: Handle how incoming data are passed to different queues
- Here use fanout exchanger: Puts a new messenge to all binded queues.
- `sender.py`: Sender, puts messenges to exchanger. (Get messenge from command line argument)
- `worker.py`: Receiver, creates new temporary custom queues. Gets messenges from queue and prints it.