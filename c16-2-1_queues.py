import queue

myqueue = queue.Queue()
myqueue.put(1.2)
myqueue.put(-4.5)
myqueue.put(8.7)

print(myqueue)

while not myqueue.empty():
    print(myqueue.get())

print(myqueue.empty())