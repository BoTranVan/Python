import requests
import threading

url = "https://google.com"
threads = []
counters = []
temp = int(input("Input number request: "))
time = 0

def sendRequest(n):
    for i in range(temp):
        while True:
            try:
                time = requests.get(url).elapsed.total_seconds()
                print "Thread: ", n, "Time total of request " ,i + 1, " is: ", time
                counters.append(time)
                if time != 0:
                    break
            except BaseException as e:
                print "Failed to establish a new connection"

for i in range(temp):
    print i
    t = threading.Thread(sendRequest(i))
    threads.append(t)
    t.start()
    
for i in counters:
    time += i
    result = time / temp

print "Avg time: ", result
print len(counters)
