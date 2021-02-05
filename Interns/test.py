import random
import threading
results	= []

def compute():
  results.append(sum(
	[random.randint(1, 100) for i in range(100000)]))

workers = [threading.Thread(target=compute) for x in range(4)]

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

print results
