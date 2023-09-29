import queue

mystack = queue.LifoQueue()
mystack.put(1.2)
mystack.put(-4.5)
mystack.put(8.7)

print(mystack)

while not mystack.empty():
    print(mystack.get())

print(mystack.empty())