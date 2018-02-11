try:
    import requests
except BaseException as e:
    print e
    
url = "http://nginx.flatbase.com"
url1 = "http://status-nginx.com/status-native"
rq01, rq02, rq03 = 0, 0, 0
process = []
temp = int(input('Input number request: '))
for i in range(temp):
    try:
        httpd1 = requests.get(url1, stream=True, timeout=1)
        sock1 = httpd1.raw._fp.fp._sock.getpeername()
        if (sock1):
            print "Send request to: ", sock1
            result1 = httpd1.text
##            print result1
            active_connection = result1.split("\n")[0]
            print active_connection
            server_rec = result1.split("\n")[2].split("\n")[0].split(" ")[1]
            if i == 0:
                process.append(server_rec)
            elif i == len(range(temp)) - 1:
                process.append(server_rec)
            client_sen = result1.split("\n")[2].split("\n")[0].split(" ")[2]
            handler = result1.split("\n")[2].split("\n")[0].split(" ")[3]
            print "Server received: ", server_rec, "\nClient sent: ", client_sen, "\nHandler request: ", handler

            
        httpd = requests.get(url, stream=True)
        sock = httpd.raw._fp.fp._sock.getpeername()
        if (sock):
            print "Send request to: ", sock
            result = httpd.text.split("Welcome to nginx on ")[1].split("!</h1>\n<p>")[0]
            print "Request ", i+1, " to host:", result
            if result == "db01":
                rq01 += 1
            elif result== "db02":
                rq02 += 1
            elif result == "db03":
                rq03 += 1
    except BaseException as e:
        print e
    
print "Request db01: ", rq01
print "Request db02: ", rq02
print "Request db03: ", rq03
print "Numbers request sent: ", (int(process[1]) - int(process[0]) + 2)
