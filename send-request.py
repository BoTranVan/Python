import requests

url = "http://192.168.8.1"

counters = []
temp = int(input("Input number request: "))
time = 0
for i in range(temp):
    while True:
        try:
            time = requests.get(url).elapsed.total_seconds()
            print "Time total of request " ,i + 1, " is: ", time
            counters.append(time)
            if time != 0:
                break
        except BaseException as e:
            print "Failed to establish a new connection"

for i in counters:
    time += i
    result = time / temp

print "Avg time: ", result
